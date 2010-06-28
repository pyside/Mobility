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

// MultimediaKit
#include <QtMultimediaKit/QAbstractAudioDeviceInfo>
#include <QtMultimediaKit/QAbstractAudioInput>
#include <QtMultimediaKit/QAbstractAudioOutput>
#include <QtMultimediaKit/QAbstractVideoBuffer>
#include <QtMultimediaKit/QAbstractVideoSurface>
#include <QtMultimediaKit/QAudioCaptureSource>
#include <QtMultimediaKit/QAudioDeviceInfo>
#include <QtMultimediaKit/QAudioEncoderControl>
#include <QtMultimediaKit/QAudioEncoderSettings>
#include <QtMultimediaKit/QAudioEndpointSelector>
#include <QtMultimediaKit/QAudioFormat>
#include <QtMultimediaKit/QAudioInput>
#include <QtMultimediaKit/QAudioOutput>
#include <QtMultimediaKit/QAudioSystemPlugin>
#include <QtMultimediaKit/QGraphicsVideoItem>
#include <QtMultimediaKit/QImageEncoderControl>
#include <QtMultimediaKit/QImageEncoderSettings>
#include <QtMultimediaKit/QLocalMediaPlaylistProvider>
#include <QtMultimediaKit/QMediaBindableInterface>
#include <QtMultimediaKit/QMediaContainerControl>
#include <QtMultimediaKit/QMediaContent>
#include <QtMultimediaKit/QMediaControl>
#include <QtMultimediaKit/QMediaImageViewer>
#include <QtMultimediaKit/QMediaObject>
#include <QtMultimediaKit/QMediaPlayer>
#include <QtMultimediaKit/QMediaPlayerControl>
#include <QtMultimediaKit/QMediaPlaylist>
#include <QtMultimediaKit/QMediaPlaylistControl>
#include <QtMultimediaKit/QMediaPlaylistIOPlugin>
#include <QtMultimediaKit/QMediaPlaylistNavigator>
#include <QtMultimediaKit/QMediaPlaylistProvider>
#include <QtMultimediaKit/QMediaPlaylistReader>
#include <QtMultimediaKit/QMediaPlaylistSourceControl>
#include <QtMultimediaKit/QMediaPlaylistWriter>
#include <QtMultimediaKit/QMediaRecorder>
#include <QtMultimediaKit/QMediaRecorderControl>
#include <QtMultimediaKit/QMediaResource>
#include <QtMultimediaKit/QMediaService>
#include <QtMultimediaKit/QMediaServiceProvider>
#include <QtMultimediaKit/QMediaServiceProviderHint>
#include <QtMultimediaKit/QMediaServiceProviderPlugin>
#include <QtMultimediaKit/QMediaStreamsControl>
#include <QtMultimediaKit/QMediaTimeInterval>
#include <QtMultimediaKit/QMediaTimeRange>
#include <QtMultimediaKit/QMetaDataReaderControl>
#include <QtMultimediaKit/QMetaDataWriterControl>
#include <QtMultimediaKit/QRadioTuner>
#include <QtMultimediaKit/QRadioTunerControl>
#include <QtMultimediaKit/QVideoDeviceControl>
#include <QtMultimediaKit/QVideoEncoderControl>
#include <QtMultimediaKit/QVideoEncoderSettings>
#include <QtMultimediaKit/QVideoFrame>
#include <QtMultimediaKit/QVideoRendererControl>
#include <QtMultimediaKit/QVideoSurfaceFormat>
#include <QtMultimediaKit/QVideoWidget>
#include <QtMultimediaKit/QVideoWidgetControl>
#include <QtMultimediaKit/QVideoWindowControl>

// Sensors
#include <QtSensors/QAccelerometerReading>
#include <QtSensors/QAccelerometerFilter>
#include <QtSensors/QAccelerometer>
#include <QtSensors/QAmbientLightReading>
#include <QtSensors/QAmbientLightFilter>
#include <QtSensors/QAmbientLightSensor>
#include <QtSensors/QCompassReading>
#include <QtSensors/QCompassFilter>
#include <QtSensors/QCompass>
#include <QtSensors/QMagnetometerReading>
#include <QtSensors/QMagnetometerFilter>
#include <QtSensors/QMagnetometer>
#include <QtSensors/QOrientationReading>
#include <QtSensors/QOrientationFilter>
#include <QtSensors/QOrientationSensor>
#include <QtSensors/QProximityReading>
#include <QtSensors/QProximityFilter>
#include <QtSensors/QProximitySensor>
#include <QtSensors/QRotationReading>
#include <QtSensors/QRotationFilter>
#include <QtSensors/QRotationSensor>
#include <QtSensors/QSensorBackend>
#include <QtSensors/QSensor>
#include <QtSensors/QSensorFilter>
#include <QtSensors/QSensorReading>
#include <QtSensors/QSensorManager>
#include <QtSensors/QSensorBackendFactory>
#include <QtSensors/QSensorPluginInterface>
#include <QtSensors/QTapReading>
#include <QtSensors/QTapFilter>
#include <QtSensors/QTapSensor>
