
import collections
import os.path
import shutil
import zipfile

from CalibrationFile import CalibrationFile


class CalibrationFileReader:

    # reads calibration files stored in directory
    @staticmethod
    def read(fp):
        calibrationMap = collections.OrderedDict()

        for (dirpath, dirnames, filenames) in os.walk(fp):
            for name in filenames:
                #print("infile:", name)
                if os.path.splitext(name)[1].lower() == ".cal" or \
                   os.path.splitext(name)[1].lower() == ".dat" or \
                   os.path.splitext(name)[1].lower() == ".ini" or \
                   os.path.splitext(name)[1].lower() == ".tdf":
                    with open(os.path.join(dirpath, name), 'rb') as f:
                        cf = CalibrationFile()
                        cf.read(f)
                        #print("id:", cf.id)
                        calibrationMap[name] = cf
            break

        return calibrationMap

    # reads calibration files stored in .sip file (renamed .zip)
    @staticmethod
    def readSip(fp):
        calibrationMap = collections.OrderedDict()

        with zipfile.ZipFile(fp, 'r') as zf:
            for finfo in zf.infolist():
                if not str(finfo.filename).startswith('__MACOSX/'):
                    print("infile:", finfo.filename)
                    if os.path.splitext(finfo.filename)[1].lower() == ".cal" or \
                        os.path.splitext(finfo.filename)[1].lower() == ".dat" or \
                            os.path.splitext(finfo.filename)[1].lower() == ".ini" or \
                    os.path.splitext(finfo.filename)[1].lower() == ".tdf":
                        with zf.open(finfo) as f:
                            cf = CalibrationFile()
                            cf.read(f)
                            #print("id:", cf.id)
                            calibrationMap[finfo.filename] = cf
                            [dest,_] = os.path.split(fp)
                            src = zf.extract(f.name,path=dest)
                            [_,fname] = os.path.split(f.name)
                            shutil.move(src, os.path.join(dest,fname))

        return calibrationMap
