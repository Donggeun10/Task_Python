# automatically generated by the FlatBuffers compiler, do not modify
from datetime import datetime, timezone

# namespace: v3

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AppLoadLogV3(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAppLoadLogV3(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AppLoadLogV3()
        x.Init(buf, n + offset)
        return x

    # AppLoadLogV3
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AppLoadLogV3
    def Model(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def Os(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def OsVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def CrashSDKVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def AppVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def PackageName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def UserKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def DeviceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def GameCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def Geo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def City(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def ReportDatetime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AppLoadLogV3
    def MemoryWarning(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def Carrier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def SessionKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def Emulator(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # AppLoadLogV3
    def NetworkKind(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def VendorUserKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AppLoadLogV3
    def VendorDeviceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    def to_dict(self):
        return {
            "receiveDatetime" : datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "model": self.Model().decode('utf-8'),
            "os": self.Os().decode('utf-8'),
            "osVersion": self.OsVersion().decode('utf-8'),
            "crashSDKVersion": self.CrashSDKVersion().decode('utf-8'),
            "appVersion": self.AppVersion().decode('utf-8'),
            "packageName": self.PackageName().decode('utf-8'),
            "userKey": self.UserKey().decode('utf-8'),
            "deviceId": self.DeviceId().decode('utf-8'),
            "gameCode": self.GameCode().decode('utf-8'),
            "geo": self.Geo().decode('utf-8'),
            "city": self.City().decode('utf-8'),
            "reportDatetime": self.ReportDatetime(),
            "memoryWarning": self.MemoryWarning().decode('utf-8'),
            "carrier": self.Carrier().decode('utf-8'),
            "sessionKey": self.SessionKey().decode('utf-8'),
            "emulator": self.Emulator(),
            "networkKind": self.NetworkKind().decode('utf-8'),
            "vendorUserKey": self.VendorUserKey().decode('utf-8'),
            "vendorDeviceId": self.VendorDeviceId().decode('utf-8')
        }

def AppLoadLogV3Start(builder): builder.StartObject(19)
def AppLoadLogV3AddModel(builder, model): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(model), 0)
def AppLoadLogV3AddOs(builder, os): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(os), 0)
def AppLoadLogV3AddOsVersion(builder, osVersion): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(osVersion), 0)
def AppLoadLogV3AddCrashSDKVersion(builder, crashSDKVersion): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(crashSDKVersion), 0)
def AppLoadLogV3AddAppVersion(builder, appVersion): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(appVersion), 0)
def AppLoadLogV3AddPackageName(builder, packageName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(packageName), 0)
def AppLoadLogV3AddUserKey(builder, userKey): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(userKey), 0)
def AppLoadLogV3AddDeviceId(builder, deviceId): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(deviceId), 0)
def AppLoadLogV3AddGameCode(builder, gameCode): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(gameCode), 0)
def AppLoadLogV3AddGeo(builder, geo): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(geo), 0)
def AppLoadLogV3AddCity(builder, city): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(city), 0)
def AppLoadLogV3AddReportDatetime(builder, reportDatetime): builder.PrependInt64Slot(11, reportDatetime, 0)
def AppLoadLogV3AddMemoryWarning(builder, memoryWarning): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(memoryWarning), 0)
def AppLoadLogV3AddCarrier(builder, carrier): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(carrier), 0)
def AppLoadLogV3AddSessionKey(builder, sessionKey): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(sessionKey), 0)
def AppLoadLogV3AddEmulator(builder, emulator): builder.PrependBoolSlot(15, emulator, 0)
def AppLoadLogV3AddNetworkKind(builder, networkKind): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(networkKind), 0)
def AppLoadLogV3AddVendorUserKey(builder, vendorUserKey): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(vendorUserKey), 0)
def AppLoadLogV3AddVendorDeviceId(builder, vendorDeviceId): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(vendorDeviceId), 0)
def AppLoadLogV3End(builder): return builder.EndObject()
