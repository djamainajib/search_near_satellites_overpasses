
def MaskClear(image):
  qa = image.select('Fmask').uint8()
  mask = qa.bitwiseAnd(1).eq(0) \
                  .And(qa.bitwiseAnd(1<<1).eq(0)) \
                  .And(qa.bitwiseAnd(1<<2).eq(0)) \
                  .And(qa.bitwiseAnd(1<<3).eq(0))
  return image.updateMask(mask)

def Cloudcover():
    return 'CLOUD_COVERAGE'

def CollectionName():
    return 'NASA/HLS/HLSL30/v002'