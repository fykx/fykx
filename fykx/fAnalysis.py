def union(datalist, pathout, geom_type, out_proj):
    from osgeo import gdal,ogr,osr
    
    #输出投影
    _out_srs = osr.SpatialReference()
    _out_srs.ImportFromProj4(out_proj)

    #建立新数据集
    _driver = ogr.GetDriverByName('ESRI Shapefile')
    _ds_0 = _driver.CreateDataSource(pathout + '/' + 'proj_' + 'out.shp')
    _out_lyr = _ds_0.CreateLayer('out', _out_srs, geom_type)

    #添加字段
    _fld = ogr.FieldDefn('name', ogr.OFTString)
    _fld.SetWidth(100)
    _out_lyr.CreateField(_fld)

    #创建空要素
    _out_feat = ogr.Feature(_out_lyr.GetLayerDefn())

    for _fn in datalist:
        _ds = ogr.Open(_fn, 0)#第二个参数0表示以只读方式打开文件
        _in_lyr = _ds.GetLayer(0)

        #当前投影
        _in_srs = _in_lyr.GetSpatialRef()

        #创建转换对象
        _ctx = osr.CoordinateTransformation(_in_srs, _out_srs)

        #写入几何、属性
        for _in_feat in _in_lyr:
            _geom = _in_feat.geometry()
            _geom.Transform(_ctx)#投影转换
            _out_feat.SetGeometry(_geom)
            for _i in range(_in_feat.GetFieldCount()):
                _out_feat.SetField(_i, _in_feat.GetField(_i))
            _out_lyr.CreateFeature(_out_feat)
    return