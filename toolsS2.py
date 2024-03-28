def MaskClear(image):
  qa = image.select('QA60')
  mask = (qa.bitwiseAnd(1<<10).eq(0)).And(qa.bitwiseAnd(1<<11).eq(0))
  return image.updateMask(mask)

def Cloudcover():
    return 'CLOUDY_PIXEL_PERCENTAGE'

def CollectionName():
    return 'COPERNICUS/S2_SR_HARMONIZED'




