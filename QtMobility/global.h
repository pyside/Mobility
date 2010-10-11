// Sensors
// QtMobility global header
#include "pyside_global.h"
#include <qmobilityglobal.h>

// Avoid problematic QLatin1Constant definition
#if (QTM_VERSION >= QTM_VERSION_CHECK(1, 1, 0))
#define QLATIN1CONSTANT_H
#else
#define QTCONTACTSGLOBAL_H
#endif
#define Q_DECLARE_LATIN1_CONSTANT(varname, str) static const QString varname

// SysInfo
#include <qsysteminfo.h>

// Location
#include <QGeoAreaMonitor>
#include <QGeoCoordinate>
#include <QGeoPositionInfo>
#include <QGeoPositionInfoSource>
#include <QGeoSatelliteInfo>
#include <QGeoSatelliteInfoSource>
#include <QNmeaPositionInfoSource>

#if (QTM_VERSION >= QTM_VERSION_CHECK(1, 1, 0))
    #include <QGeoAddress>
    #include <QGeoBoundingArea>
    #include <QGeoBoundingBox>
    #include <QGeoBoundingCircle>
    #include <QGeoManeuver>
    #include <QGeoMapCircleObject>
    #include <QGeoMapData>
    #include <QGeoMapGroupObject>
    #include <QGeoMapObject>
    #include <QGeoMapObjectInfo>
    #include <QGeoMapOverlay>
    #include <QGeoMappingManager>
    #include <QGeoMappingManagerEngine>
    #include <QGeoMapPixmapObject>
    #include <QGeoMapPolygonObject>
    #include <QGeoMapPolylineObject>
    #include <QGeoMapRectangleObject>
    #include <QGeoMapRouteObject>
    #include <QGeoMapTextObject>
    #include <QGeoPlace>
    #include <QGeoRoute>
    #include <QGeoRouteReply>
    #include <QGeoRouteRequest>
    #include <QGeoRouteSegment>
    #include <QGeoRoutingManager>
    #include <QGeoRoutingManagerEngine>
    #include <QGeoSearchManager>
    #include <QGeoSearchManagerEngine>
    #include <QGeoSearchReply>
    #include <QGeoServiceProvider>
    #include <QGeoServiceProviderFactory>
    #include <QGeoTiledMapData>
    #include <QGeoTiledMappingManagerEngine>
    #include <QGeoTiledMapReply>
    #include <QGeoTiledMapRequest>
    #include <QGraphicsGeoMap>
    #include <QLandmark>
    #include <QLandmarkAbstractRequest>
    #include <QLandmarkAttributeFilter>
    #include <QLandmarkBoxFilter>
    #include <QLandmarkCategory>
    #include <QLandmarkCategoryFetchByIdRequest>
    #include <QLandmarkCategoryFetchRequest>
    #include <QLandmarkCategoryFilter>
    #include <QLandmarkCategoryId>
    #include <QLandmarkCategoryIdFetchRequest>
    #include <QLandmarkCategoryRemoveRequest>
    #include <QLandmarkCategorySaveRequest>
    #include <QLandmarkExportRequest>
    #include <QLandmarkFetchByIdRequest>
    #include <QLandmarkFetchRequest>
    #include <QLandmarkFilter>
    #include <QLandmarkId>
    #include <QLandmarkIdFetchRequest>
    #include <QLandmarkIdFilter>
    #include <QLandmarkImportRequest>
    #include <QLandmarkIntersectionFilter>
    #include <QLandmarkManager>
    #include <QLandmarkManagerEngine>
    #include <QLandmarkManagerEngineFactory>
    #include <QLandmarkNameFilter>
    #include <QLandmarkNameSort>
    #include <QLandmarkProximityFilter>
    #include <QLandmarkRemoveRequest>
    #include <QLandmarkSaveRequest>
    #include <QLandmarkSortOrder>
    #include <QLandmarkUnionFilter>
#endif

// Bearer
#if(QT_VERSION < QT_VERSION_CHECK(4, 7, 0))
#include <QNetworkConfiguration>
#include <QNetworkConfigurationManager>
#include <QNetworkSession>
#endif

// Contacts
#include <qtcontacts.h>
#include <qcontactchangeset.h>

// Feedback
#include <QFeedbackActuator>
#include <QFeedbackEffect>
#include <QFeedbackHapticsEffect>
#include <QFeedbackFileEffect>
#include <QFeedbackInterface>
#include <QFeedbackHapticsInterface>
#include <QFeedbackFileInterface>

// Gallery
#include <QAbstractGallery>
#include <QDocumentGallery>
#include <QGalleryAbstractRequest>
#include <QGalleryAbstractResponse>
#include <QGalleryFilter>
#include <QGalleryIntersectionFilter>
#include <QGalleryItemRequest>
#include <QGalleryMetaDataFilter>
#include <QGalleryProperty>
#include <QGalleryQueryModel>
#include <QGalleryQueryRequest>
#include <QGalleryResource>
#include <QGalleryResultSet>
#include <QGalleryType>
#include <QGalleryTypeRequest>
#include <QGalleryUnionFilter>

// MultimediaKit
#include <QAbstractAudioDeviceInfo>
#include <QAbstractAudioInput>
#include <QAbstractAudioOutput>
#include <QAbstractVideoBuffer>
#include <QAbstractVideoSurface>
#include <QAudioCaptureSource>
#include <QAudioDeviceInfo>
#include <QAudioEncoderControl>
#include <QAudioEncoderSettings>
#include <QAudioEndpointSelector>
#include <QAudioFormat>
#include <QAudioInput>
#include <QAudioOutput>
#include <QAudioSystemPlugin>
#include <QGraphicsVideoItem>
#include <QImageEncoderControl>
#include <QImageEncoderSettings>
#include <QLocalMediaPlaylistProvider>
#include <QMediaBindableInterface>
#include <QMediaContainerControl>
#include <QMediaContent>
#include <QMediaControl>
#include <QMediaImageViewer>
#include <QMediaObject>
#include <QMediaPlayer>
#include <QMediaPlayerControl>
#include <QMediaPlaylist>
#include <QMediaPlaylistControl>
#include <QMediaPlaylistIOPlugin>
#include <QMediaPlaylistNavigator>
#include <QMediaPlaylistProvider>
#include <QMediaPlaylistReader>
#include <QMediaPlaylistSourceControl>
#include <QMediaPlaylistWriter>
#include <QMediaRecorder>
#include <QMediaRecorderControl>
#include <QMediaResource>
#include <QMediaService>
#include <QMediaServiceProvider>
#include <QMediaServiceProviderHint>
#include <QMediaServiceProviderPlugin>
#include <QMediaStreamsControl>
#include <QMediaTimeInterval>
#include <QMediaTimeRange>
#include <QMetaDataReaderControl>
#include <QMetaDataWriterControl>
#include <QRadioTuner>
#include <QRadioTunerControl>
#include <QVideoDeviceControl>
#include <QVideoEncoderControl>
#include <QVideoEncoderSettings>
#include <QVideoFrame>
#include <QVideoRendererControl>
#include <QVideoSurfaceFormat>
#include <QVideoWidget>
#include <QVideoWidgetControl>
#include <QVideoWindowControl>

//Organizer
//avoid header inclusion
#define QTORGANIZERGLOBAL_H
#define QTORGANIZER_VERSION_NAME "com.nokia.qt.mobility.organizer.api.version"
#define QTORGANIZER_IMPLEMENTATION_VERSION_NAME "com.nokia.qt.mobility.organizer.implementation.version"
#define QTORGANIZER_VERSION 1

#include <QOrganizerCollection>
#include <QOrganizerCollectionEngineLocalId>
#include <QOrganizerCollectionId>
#include <QOrganizerCollectionLocalId>
#include <QOrganizerCollectionRemoveRequest>
#include <QOrganizerCollectionSaveRequest>
#include <QOrganizerEvent>
#include <QOrganizerEventOccurrence>
#include <QOrganizerEventTimeRange>
#include <QOrganizerItem>
#include <QOrganizerItemAbstractRequest>
#include <QOrganizerItemAudibleReminder>
#include <QOrganizerItemCollectionFilter>
#include <QOrganizerItemComment>
#include <QOrganizerItemDateTimePeriodFilter>
#include <QOrganizerItemDescription>
#include <QOrganizerItemDetail>
#include <QOrganizerItemDetailDefinition>
#include <QOrganizerItemDetailDefinitionRemoveRequest>
#include <QOrganizerItemDetailDefinitionSaveRequest>
#include <QOrganizerItemDetailFieldDefinition>
#include <QOrganizerItemDetailFilter>
#include <QOrganizerItemDetailRangeFilter>
#include <QOrganizerItemDisplayLabel>
#include <QOrganizerItemEmailReminder>
#include <QOrganizerItemEngineLocalId>
#include <QOrganizerItemFilter>
#include <QOrganizerItemGuid>
#include <QOrganizerItemId>
#include <QOrganizerItemInstanceOrigin>
#include <QOrganizerItemIntersectionFilter>
#include <QOrganizerItemInvalidFilter>
#include <QOrganizerItemLocalId>
#include <QOrganizerItemLocalIdFilter>
#include <QOrganizerItemLocation>
#include <QOrganizerItemManager>
#include <QOrganizerItemManagerEngine>
#include <QOrganizerItemManagerEngineFactory>
#include <QOrganizerItemPriority>
#include <QOrganizerItemRecurrence>
#include <QOrganizerItemRecurrenceRule>
#include <QOrganizerItemReminder>
#include <QOrganizerItemRemoveRequest>
#include <QOrganizerItemSaveRequest>
#include <QOrganizerItemSortOrder>
#include <QOrganizerItemTimestamp>
#include <QOrganizerItemType>
#include <QOrganizerItemUnionFilter>
#include <QOrganizerItemVisualReminder>
#include <QOrganizerJournal>
#include <QOrganizerJournalTimeRange>
#include <QOrganizerNote>
#include <QOrganizerTodo>
#include <QOrganizerTodoOccurrence>
#include <QOrganizerTodoProgress>
#include <QOrganizerTodoTimeRange>



// Sensors
#include <QAccelerometerReading>
#include <QAccelerometerFilter>
#include <QAccelerometer>
#include <QAmbientLightReading>
#include <QAmbientLightFilter>
#include <QAmbientLightSensor>
#include <QCompassReading>
#include <QCompassFilter>
#include <QCompass>
#include <QMagnetometerReading>
#include <QMagnetometerFilter>
#include <QMagnetometer>
#include <QOrientationReading>
#include <QOrientationFilter>
#include <QOrientationSensor>
#include <QProximityReading>
#include <QProximityFilter>
#include <QProximitySensor>
#include <QRotationReading>
#include <QRotationFilter>
#include <QRotationSensor>
#include <QSensorBackend>
#include <QSensor>
#include <QSensorFilter>
#include <QSensorReading>
#include <QSensorManager>
#include <QSensorBackendFactory>
#include <QSensorPluginInterface>
#include <QTapReading>
#include <QTapFilter>
#include <QTapSensor>

//Versit
#include <QVersitContactExporter>
#include <QVersitContactExporterDetailHandler>
#include <QVersitContactImporter>
#include <QVersitContactImporterPropertyHandler>
#include <QVersitDefaultResourceHandler>
#include <QVersitDocument>
#include <QVersitProperty>
#include <QVersitReader>
#include <QVersitResourceHandler>
#include <QVersitWriter>

// Messaging
#include <qmessage.h>
#include <qmessageaccount.h>
#include <qmessageaccountfilter.h>
#include <qmessageaccountid.h>
#include <qmessageaccountsortorder.h>
#include <qmessageaddress.h>
#include <qmessagecontentcontainer.h>
#include <qmessagecontentcontainerid.h>
#include <qmessagefilter.h>
#include <qmessagefolder.h>
#include <qmessagefolderfilter.h>
#include <qmessagefolderid.h>
#include <qmessagefoldersortorder.h>
#include <qmessageid.h>
#include <qmessagemanager.h>
#include <qmessageservice.h>
#include <qmessagesortorder.h>
#include <qmessagestore.h>

// ServiceFramework
#include <QAbstractSecuritySession>
#include <QServiceContext>
#include <QServiceFilter>
#include <QServiceInterfaceDescriptor>
#include <QServiceManager>
#include <QServicePluginInterface>
#include <qremoteserviceclassregister.h> // where is the include without .h like the others?
#include <qremoteservicecontrol.h>       // where is the include without .h like the others?

// PublishSubscribe
#include <QValueSpacePublisher>
#include <QValueSpaceSubscriber>

