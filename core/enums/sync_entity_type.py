from django.db import models


class SyncEntityType(models.TextChoices):
    AUTHUSERV1 = 'AuthUserV1', 'AuthUserV1',

    USERV1 = 'UserV1', 'UserV1',
    USERDELETEV1 = 'UserDeleteV1', 'UserDeleteV1',

    ASSETV1 = 'AssetV1', 'AssetV1',
    ASSETV2 = 'AssetV2', 'AssetV2',
    ASSETDELETEV1 = 'AssetDeleteV1', 'AssetDeleteV1',
    ASSETEXIFV1 = 'AssetExifV1', 'AssetExifV1',
    ASSETEDITV1 = 'AssetEditV1', 'AssetEditV1',
    ASSETEDITDELETEV1 = 'AssetEditDeleteV1', 'AssetEditDeleteV1',
    ASSETMETADATAV1 = 'AssetMetadataV1', 'AssetMetadataV1',
    ASSETMETADATADELETEV1 = 'AssetMetadataDeleteV1', 'AssetMetadataDeleteV1',

    PARTNERV1 = 'PartnerV1', 'PartnerV1',
    PARTNERDELETEV1 = 'PartnerDeleteV1', 'PartnerDeleteV1',
    PARTNERASSETV1 = 'PartnerAssetV1', 'PartnerAssetV1',
    PARTNERASSETV2 = 'PartnerAssetV2', 'PartnerAssetV2',
    PARTNERASSETBACKFILLV1 = 'PartnerAssetBackfillV1', 'PartnerAssetBackfillV1',
    PARTNERASSETBACKFILLV2 = 'PartnerAssetBackfillV2', 'PartnerAssetBackfillV2',
    PARTNERASSETDELETEV1 = 'PartnerAssetDeleteV1', 'PartnerAssetDeleteV1',
    PARTNERASSETEXIFV1 = 'PartnerAssetExifV1', 'PartnerAssetExifV1',
    PARTNERASSETEXIFBACKFILLV1 = 'PartnerAssetExifBackfillV1', 'PartnerAssetExifBackfillV1',
    PARTNERSTACKBACKFILLV1 = 'PartnerStackBackfillV1', 'PartnerStackBackfillV1',
    PARTNERSTACKDELETEV1 = 'PartnerStackDeleteV1', 'PartnerStackDeleteV1',
    PARTNERSTACKV1 = 'PartnerStackV1', 'PartnerStackV1',

    ALBUMV1 = 'AlbumV1', 'AlbumV1',
    ALBUMV2 = 'AlbumV2', 'AlbumV2',
    ALBUMDELETEV1 = 'AlbumDeleteV1', 'AlbumDeleteV1',
    ALBUMUSERV1 = 'AlbumUserV1', 'AlbumUserV1',
    ALBUMUSERBACKFILLV1 = 'AlbumUserBackfillV1', 'AlbumUserBackfillV1',
    ALBUMUSERDELETEV1 = 'AlbumUserDeleteV1', 'AlbumUserDeleteV1',
    ALBUMASSETCREATEV1 = 'AlbumAssetCreateV1', 'AlbumAssetCreateV1',
    ALBUMASSETCREATEV2 = 'AlbumAssetCreateV2', 'AlbumAssetCreateV2',
    ALBUMASSETUPDATEV1 = 'AlbumAssetUpdateV1', 'AlbumAssetUpdateV1',
    ALBUMASSETUPDATEV2 = 'AlbumAssetUpdateV2', 'AlbumAssetUpdateV2',
    ALBUMASSETBACKFILLV1 = 'AlbumAssetBackfillV1', 'AlbumAssetBackfillV1',
    ALBUMASSETBACKFILLV2 = 'AlbumAssetBackfillV2', 'AlbumAssetBackfillV2',
    ALBUMASSETEXIFCREATEV1 = 'AlbumAssetExifCreateV1', 'AlbumAssetExifCreateV1',
    ALBUMASSETEXIFUPDATEV1 = 'AlbumAssetExifUpdateV1', 'AlbumAssetExifUpdateV1',
    ALBUMASSETEXIFBACKFILLV1 = 'AlbumAssetExifBackfillV1', 'AlbumAssetExifBackfillV1',
    ALBUMTOASSETV1 = 'AlbumToAssetV1', 'AlbumToAssetV1',
    ALBUMTOASSETDELETEV1 = 'AlbumToAssetDeleteV1', 'AlbumToAssetDeleteV1',
    ALBUMTOASSETBACKFILLV1 = 'AlbumToAssetBackfillV1', 'AlbumToAssetBackfillV1',

    MEMORYV1 = 'MemoryV1', 'MemoryV1',
    MEMORYDELETEV1 = 'MemoryDeleteV1', 'MemoryDeleteV1',
    MEMORYTOASSETV1 = 'MemoryToAssetV1', 'MemoryToAssetV1',
    MEMORYTOASSETDELETEV1 = 'MemoryToAssetDeleteV1', 'MemoryToAssetDeleteV1',

    STACKV1 = 'StackV1', 'StackV1',
    STACKDELETEV1 = 'StackDeleteV1', 'StackDeleteV1',

    PERSONV1 = 'PersonV1', 'PersonV1',
    PERSONDELETEV1 = 'PersonDeleteV1', 'PersonDeleteV1',

    ASSETFACEV1 = 'AssetFaceV1', 'AssetFaceV1',
    ASSETFACEV2 = 'AssetFaceV2', 'AssetFaceV2',
    ASSETFACEDELETEV1 = 'AssetFaceDeleteV1', 'AssetFaceDeleteV1',

    USERMETADATAV1 = 'UserMetadataV1', 'UserMetadataV1',
    USERMETADATADELETEV1 = 'UserMetadataDeleteV1', 'UserMetadataDeleteV1',

    SYNCACKV1 = 'SyncAckV1', 'SyncAckV1',
    SYNCRESETV1 = 'SyncResetV1', 'SyncResetV1',
    SYNCCOMPLETEV1 = 'SyncCompleteV1', 'SyncCompleteV1',
