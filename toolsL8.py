def MaskClear(image):
  qa = image.select('QA_PIXEL').uint16()
  mask = qa.bitwiseAnd(1).eq(0) \
                  .And(qa.bitwiseAnd(1<<2).eq(0)) \
                  .And(qa.bitwiseAnd(1<<3).eq(0)) \
                  .And(qa.bitwiseAnd(1<<4).eq(0)) \
                  .And(qa.bitwiseAnd(1<<5).eq(0)) 
  return image.updateMask(mask)

def Cloudcover():
    return 'CLOUD_COVER_LAND'

def CollectionName():
    return 'LANDSAT/LC08/C02/T1_L2'

