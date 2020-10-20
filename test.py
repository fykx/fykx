from fykx.f3DAnalyst import raster_extent

def listdatas(pathin):
    import os

    _datas = []
    _names = []
    for _root, _dirs, _files in os.walk(pathin):
        if len(_files) != 0:
            for _file in _files:
                _names.append(_file.split("_")[0])
                _vv = None
                if _file.endswith('.tif'):
                   _vv = os.path.join(_root, _file)
                   _datas.append(_vv)

    _mosaic_datas = []               
    for _name in list(set(_names)):
        for _data in _datas:
            if _data.split('/')[-1].split('_')[0] == _name:
                _mosaic_datas.append(_data)
                break
    return _mosaic_datas



def main():
    pathin = r'/mnt/e/r1'
    pathout = r'/mnt/e/r1/out'
    datas = listdatas(pathin)
    for data in datas:
        raster_extent(data, pathout)
    return


if __name__ == '__main__':
    main()

