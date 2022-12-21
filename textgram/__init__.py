from typing import List, Iterable
import collections


def distplot(
  data: List,
  increment_y: int = 1,
  increment_x: int = 1,
  spacing_y: int = 30,
  spacing_x: int = 30,
  label_y: str = 'p(x)',
  label_x: str = 'x'
  character_bar: str = '#',
  character_divider: str = '_',
) -> str:
  """
  Renders a normalized histogram of the frequencies at
  which different elements in a list occur.
  
  
  Parameters
  ----------
  
  data: List
  
    A list containing hashable elements.
   
  increment_y: int = 1
  
    The vertical increment to use when rendering the 
    histogram. For example a value of 2 means that every
    rendered bar character represents two vertical units.
  
  increment_x: int = 1
  
    The horizontal increment to use when rendering the
    histogram. The default value of 1 means that all data
    elements will be show.
 
  spacing_y: int = 30
  
    The height of each individual bar character.
  
  spacing_x: int = 30
  
    The space between element values.
  
  label_x: str = 'x'
  
    A label for the x-axis.
 
  label_y: str = 'p(x)'
  
    A lebel for the y-axis.
  
  character_bar: str = '#'
  
    The character to use for the histogram bars. Other
    typical values are '#' and '*'.
    
  character_divider: str = '_'
  
    The character to use for the histogram divider.
  
  
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
  
  counter = collections.Counter(data)
  
  
