"""
    Amtex Training Project
    "Image Upload Program"
       
      Sandeep Jadoonanan
       October 24, 2014
"""

def getSize(amt):
  """
  This function takes a file size (in bytes) and converts
  the output into readable format. Supports file sizes in:
  'bytes', 'kb',  and 'mb'.
  """
  fmt = lambda x: "{:,}".format(x)
  fstr = lambda x, y: float("%.1f" % (x / float(y)))
  kb = 1024
  mb = (1024 * 1024)
   
  if amt >= mb:
    amt = fmt(fstr(amt, mb)) + " mb"
    return amt 
   
  if amt >= kb:
    amt = fmt(fstr(amt, kb)) + " kb"
    return amt
   
  return fmt(amt) + " bytes"