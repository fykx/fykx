from fykx.fos import listdatas
from fykx.fAnalysis import union


def main():
    pathin = r'/mnt/e/r1/out'
    pathout = r'/mnt/e/r1'
    datalist = listdatas(pathin, '.shp')
    geom_type = ogr.wkbPolygon
    out_proj = '''+proj=aea +lat_1=25 +lat_2=47 +lat_0=0 +lon_0=105 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs'''
    union(datalist, pathout, geom_type, out_proj)

if __name__ == '__main__':
    main()