from typing import List, Iterable
import collections


# TODO: clean this up - very messy currently (but it does work).


def distplot(
  data: List[int],
  increment_y: int = 1,
  increment_x: int = 1,
  spacing_y: int = 2,
  spacing_x: int = 2,
  label_y: str = 'p(x)',
  label_x: str = 'x',
  character_bar: str = '#',
  character_margin: str = '_',
) -> str:
  """
  Renders a normalized histogram of the frequencies at
  which different elements in a list occur.


  Parameters
  ----------

  data: List[int]

    A list containing hashable elements.

  increment_y: int = 1

    The vertical increment to use when rendering the
    histogram. For example a value of 2 means that every
    rendered bar character represents two vertical units.

  increment_x: int = 1

    The horizontal increment to use when rendering the
    histogram. The default value of 1 means that buckets
    will contain only one data element.

  spacing_y: int = 2

    The height of each individual bar character.

  spacing_x: int = 2

    The space between element values.

  label_x: str = 'x'

    A label for the x-axis.

  label_y: str = 'p(x)'

    A label for the y-axis.

  character_bar: str = '#'

    The character to use for the histogram bars. Other
    typical values are '#' and '*'.

  character_margin: str = '_'

    The character to use for the axis margins.


  Returns
  -------

  render: str

    The rendered histogram.


  Examples
  --------

  >>> import textgram as tg
  >>> data = [1,1,1,2,1,1,2,1,2,3]
  >>> print(tg.distplot(data))

  P(X)

  | #
  | #
  | #
  | #  #
  | #  #
  | #  #  #
  +--------- X
    1  2  3

  >>>
  """

  assert len(data) > 0
  assert len(character_bar) == 1
  assert len(character_margin) == 1
  assert increment_x > 0
  assert increment_y > 0
  assert spacing_y > 0
  assert spacing_x > 0

  if spacing_x % 2 != 0:
    spacing_x += 1

  # Compute bucketed frequency counts...

  counter = collections.Counter(data)
  total_count = len(data)

  counts = [(key, counter[key]) for key in range(min(counter), max(counter) + 1)]
  chunks = [counts[i : i + increment_x] for i in range(0, len(counts), increment_x)]
  chunks = [(chunk[0][0], sum([c[1] for c in chunk])) for chunk in chunks]


  # Compute the total width and height of the diagram...

  chunk_count = len(chunks)

  chunk_width = max([len(str(chunk[0])) for chunk in chunks])
  render_width = (chunk_width * chunk_count) + (spacing_x * chunk_count) # the chunks and chunk spaces.
  render_width += 2 + len(label_x) # the x-axis label and y-axis margin.

  chunk_height = (max(counter.values()) // increment_y) + 1
  chunk_height *= spacing_y
  render_height = chunk_height + 4 # the x-axis margin and y-axis label.


  # Render the histogram...

  render = [[' ' for _ in range(render_width)] for __ in range(render_height)]


  # Render the bars...

  chunk_x = 1 + (spacing_x // 2)

  for key, count in chunks:
    bar_height = int(chunk_height * (count / total_count)) * spacing_y

    for chunk_y in range(1, bar_height + 1):
      render[-2 - chunk_y][chunk_x] = character_bar

    chunk_label = [' ']*chunk_width
    chunk_label[: -1] = str(key)

    render[-1][chunk_x : chunk_x + chunk_width] = ''.join(chunk_label)
    chunk_x += chunk_width + spacing_x


  # Render the x-axis...

  render[-2] = '+' + ('-' * (render_width - 3)) + f' {label_x}'


  # Render the y-axis...

  for y in range(2, render_height - 2):
    render[y][0] = '|'

  render[0][: -1] = label_y
  return render
