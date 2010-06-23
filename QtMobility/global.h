// Sensors
// QtMobility global header


#include "pyside_global.h"
#include <qmobilityglobal.h>


// SysInfo
#include <QtSystemInfo/qsysteminfo.h>

// Location
#include <QtLocation/QGeoAreaMonitor>
#include <QtLocation/QGeoCoordinate>
#include <QtLocation/QGeoPositionInfo>
#include <QtLocation/QGeoPositionInfoSource>
#include <QtLocation/QGeoSatelliteInfo>
#include <QtLocation/QGeoSatelliteInfoSource>
#include <QtLocation/QNmeaPositionInfoSource>

// Bearer
#include <QtBearer/QNetworkConfiguration>
#include <QtBearer/QNetworkConfigurationManager>
#include <QtBearer/QNetworkSession>

// Contacts
typedef QLatin1String QLatin1Constant;// replace type
#define QTCONTACTSGLOBAL_H // avoid define template
#include <QtContacts/qtcontacts.h>
#include <QtContacts/qcontactchangeset.h>
