# DIM
DIM is a django based reimplementation of [Immich](https://github.com/immich-app/immich) (to version 2.7.5)

## Why
There are a couple of reason, although they're not tied to the Immich project doing something bad per-se:
- "Native" S3 support. What actually I need most right now. As I share Immich with my friend, I need it to be always online and fast, which currently my PC and my internet with 20 mbps upload can't. As VPS usually don't allow much storage on disk (current VPS at 12 euros is 80GB against more than half TB needed), S3 is a cheap good alternative (same host provider gives 7euro/TB/mo, as I have domain and vps, having also some s3 storage seem like a good alternative to a way higher priced VPS)
- I'm building another project about public transit, also in django. By reimplementing an actual big and complex project, I'll be bound to see and think about how to do things and design them, which I think would be helpful for my own projects.
- I'm thinking about creating my own ecosystem: photo platform, drive, calendar, contacts and so on. It would be different, as I was thinking about a plain/encrypted/hybrid approach to all of these. Again, by reimplementing Immich I'll be seeing how all components are designed and interact with each other, and also be able to understand something more about photos for the future.

## Reimplemented endpoints
Here is a list of what's missing, what works, what is work-in-progress:

<details>
<summary>API Keys</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /api-keys | getApiKeys | :orange_square: <sup>2</sup> <sup>4</sup> |
| POST | /api-keys | createApiKey | :red_square: |
| GET | /api-keys/me | getMyApiKey | :red_square: |
| GET | /api-keys/{id} | getApiKey | :red_square: |
| PUT | /api-keys/{id} | updateApiKey | :red_square: |
| DELETE | /api-keys/{id} | deleteApiKey | :red_square: |

</details>


<details>
<summary>Activity</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /activities | getActivities | :red_square: |
| POST | /activities | createActivity | :red_square: |
| GET | /activities/statistics | getActivityStatistics | :red_square: |
| DELETE | /activities/{id} | deleteActivity | :red_square: |

</details>


<details>
<summary>Albums</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /albums | getAllAlbums | :red_square: |
| POST | /albums | createAlbum | :red_square: |
| PUT | /albums/assets | addAssetsToAlbums | :red_square: |
| GET | /albums/statistics | getAlbumStatistics | :red_square: |
| GET | /albums/{id} | getAlbumInfo | :red_square: |
| DELETE | /albums/{id} | deleteAlbum | :red_square: |
| PATCH | /albums/{id} | updateAlbumInfo | :red_square: |
| PUT | /albums/{id}/assets | addAssetsToAlbum | :red_square: |
| DELETE | /albums/{id}/assets | removeAssetFromAlbum | :red_square: |
| PUT | /albums/{id}/user/{userId} | updateAlbumUser | :red_square: |
| DELETE | /albums/{id}/user/{userId} | removeUserFromAlbum | :red_square: |
| PUT | /albums/{id}/users | addUsersToAlbum | :red_square: |

</details>


<details>
<summary>Assets</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| PUT | /assets | updateAssets | :red_square: |
| POST | /assets | uploadAsset | :red_square: |
| DELETE | /assets | deleteAssets | :red_square: |
| POST | /assets/bulk-upload-check | checkBulkUpload | :red_square: |
| PUT | /assets/copy | copyAsset | :red_square: |
| POST | /assets/exist | checkExistingAssets | :red_square: |
| POST | /assets/jobs | runAssetJobs | :red_square: |
| PUT | /assets/metadata | updateBulkAssetMetadata | :red_square: |
| DELETE | /assets/metadata | deleteBulkAssetMetadata | :red_square: |
| GET | /assets/statistics | getAssetStatistics | :red_square: |
| GET | /assets/{id} | getAssetInfo | :red_square: |
| PUT | /assets/{id} | updateAsset | :red_square: |
| GET | /assets/{id}/edits | getAssetEdits | :red_square: |
| PUT | /assets/{id}/edits | editAsset | :red_square: |
| DELETE | /assets/{id}/edits | removeAssetEdits | :red_square: |
| GET | /assets/{id}/metadata | getAssetMetadata | :red_square: |
| PUT | /assets/{id}/metadata | updateAssetMetadata | :red_square: |
| GET | /assets/{id}/metadata/{key} | getAssetMetadataByKey | :red_square: |
| DELETE | /assets/{id}/metadata/{key} | deleteAssetMetadata | :red_square: |
| GET | /assets/{id}/ocr | getAssetOcr | :red_square: |
| GET | /assets/{id}/original | downloadAsset | :red_square: |
| GET | /assets/{id}/thumbnail | viewAsset | :red_square: |
| GET | /assets/{id}/video/playback | playAssetVideo | :red_square: |

</details>


<details>
<summary>Authentication</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| POST | /auth/admin-sign-up | signUpAdmin | :red_square: |
| POST | /auth/change-password | changePassword | :red_square: |
| POST | /auth/login | login | :yellow_square: <sup>1</sup>|
| POST | /auth/logout | logout | :yellow_square: <sup>3</sup>|
| PUT | /auth/pin-code | changePinCode | :red_square: |
| POST | /auth/pin-code | setupPinCode | :red_square: |
| DELETE | /auth/pin-code | resetPinCode | :red_square: |
| POST | /auth/session/lock | lockAuthSession | :red_square: |
| POST | /auth/session/unlock | unlockAuthSession | :red_square: |
| GET | /auth/status | getAuthStatus | :red_square: |
| POST | /auth/validateToken | validateAccessToken | :green_square: |
| POST | /oauth/authorize | startOAuth | :red_square: |
| POST | /oauth/callback | finishOAuth | :red_square: |
| POST | /oauth/link | linkOAuthAccount | :red_square: |
| GET | /oauth/mobile-redirect | redirectOAuthToMobile | :red_square: |
| POST | /oauth/unlink | unlinkOAuthAccount | :red_square: |

</details>


<details>
<summary>Authentication (admin)</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| POST | /admin/auth/unlink-all | unlinkAllOAuthAccountsAdmin | :red_square: |

</details>


<details>
<summary>Database Backups (admin)</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /admin/database-backups | listDatabaseBackups | :red_square: |
| DELETE | /admin/database-backups | deleteDatabaseBackup | :red_square: |
| POST | /admin/database-backups/start-restore | startDatabaseRestoreFlow | :red_square: |
| POST | /admin/database-backups/upload | uploadDatabaseBackup | :red_square: |
| GET | /admin/database-backups/{filename} | downloadDatabaseBackup | :red_square: |

</details>


<details>
<summary>Download</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| POST | /download/archive | downloadArchive | :red_square: |
| POST | /download/info | getDownloadInfo | :red_square: |

</details>


<details>
<summary>Duplicates</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /duplicates | getAssetDuplicates | :red_square: |
| DELETE | /duplicates | deleteDuplicates | :red_square: |
| POST | /duplicates/resolve | resolveDuplicates | :red_square: |
| DELETE | /duplicates/{id} | deleteDuplicate | :red_square: |

</details>


<details>
<summary>Faces</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /faces | getFaces | :red_square: |
| POST | /faces | createFace | :red_square: |
| PUT | /faces/{id} | reassignFacesById | :red_square: |
| DELETE | /faces/{id} | deleteFace | :red_square: |

</details>


<details>
<summary>Jobs</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| POST | /jobs | createJob | :red_square: |

</details>


<details>
<summary>Libraries</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /libraries | getAllLibraries | :red_square: |
| POST | /libraries | createLibrary | :red_square: |
| GET | /libraries/{id} | getLibrary | :red_square: |
| PUT | /libraries/{id} | updateLibrary | :red_square: |
| DELETE | /libraries/{id} | deleteLibrary | :red_square: |
| POST | /libraries/{id}/scan | scanLibrary | :red_square: |
| GET | /libraries/{id}/statistics | getLibraryStatistics | :red_square: |
| POST | /libraries/{id}/validate | validate | :red_square: |

</details>


<details>
<summary>Maintenance (admin)</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| POST | /admin/maintenance | setMaintenanceMode | :red_square: |
| GET | /admin/maintenance/detect-install | detectPriorInstall | :red_square: |
| POST | /admin/maintenance/login | maintenanceLogin | :red_square: |
| GET | /admin/maintenance/status | getMaintenanceStatus | :red_square: |
</details>


<details>
<summary>Map</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /map/markers | getMapMarkers | :red_square: |
| GET | /map/reverse-geocode | reverseGeocode | :red_square: |

</details>


<details>
<summary>Memories</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /memories | searchMemories | :red_square: |
| POST | /memories | createMemory | :red_square: |
| GET | /memories/statistics | memoriesStatistics | :red_square: |
| GET | /memories/{id} | getMemory | :red_square: |
| PUT | /memories/{id} | updateMemory | :red_square: |
| DELETE | /memories/{id} | deleteMemory | :red_square: |
| PUT | /memories/{id}/assets | addMemoryAssets | :red_square: |
| DELETE | /memories/{id}/assets | removeMemoryAssets | :red_square: |

</details>


<details>
<summary>Notifications</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /notifications | getNotifications | :red_square: |
| PUT | /notifications | updateNotifications | :red_square: |
| DELETE | /notifications | deleteNotifications | :red_square: |
| GET | /notifications/{id} | getNotification | :red_square: |
| PUT | /notifications/{id} | updateNotification | :red_square: |
| DELETE | /notifications/{id} | deleteNotification | :red_square: |

</details>


<details>
<summary>Notifications (admin)</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| POST | /admin/notifications | createNotification | :red_square: |
| POST | /admin/notifications/templates/{name} | getNotificationTemplateAdmin | :red_square: |
| POST | /admin/notifications/test-email | sendTestEmailAdmin | :red_square: |

</details>


<details>
<summary>Partners</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /partners | getPartners | :red_square: |
| POST | /partners | createPartner | :red_square: |
| PUT | /partners/{id} | updatePartner | :red_square: |
| DELETE | /partners/{id} | removePartner | :red_square: |
</details>


<details>
<summary>People</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /people | getAllPeople | :red_square: |
| PUT | /people | updatePeople | :red_square: |
| POST | /people | createPerson | :red_square: |
| DELETE | /people | deletePeople | :red_square: |
| GET | /people/{id} | getPerson | :red_square: |
| PUT | /people/{id} | updatePerson | :red_square: |
| DELETE | /people/{id} | deletePerson | :red_square: |
| POST | /people/{id}/merge | mergePerson | :red_square: |
| PUT | /people/{id}/reassign | reassignFaces | :red_square: |
| GET | /people/{id}/statistics | getPersonStatistics | :red_square: |
| GET | /people/{id}/thumbnail | getPersonThumbnail | :red_square: |

</details>


<details>
<summary>Plugins</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /plugins | getPlugins | :red_square: |
| GET | /plugins/triggers | getPluginTriggers | :red_square: |
| GET | /plugins/{id} | getPlugin | :red_square: |

</details>


<details>
<summary>Queues</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /queues | getQueues | :red_square: |
| GET | /queues/{name} | getQueue | :red_square: |
| PUT | /queues/{name} | updateQueue | :red_square: |
| GET | /queues/{name}/jobs | getQueueJobs | :red_square: |
| DELETE | /queues/{name}/jobs | emptyQueue | :red_square: |

</details>


<details>
<summary>Search</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /search/cities | getAssetsByCity | :red_square: |
| GET | /search/explore | getExploreData | :red_square: |
| POST | /search/large-assets | searchLargeAssets | :red_square: |
| POST | /search/metadata | searchAssets | :red_square: |
| GET | /search/person | searchPerson | :red_square: |
| GET | /search/places | searchPlaces | :red_square: |
| POST | /search/random | searchRandom | :red_square: |
| POST | /search/smart | searchSmart | :red_square: |
| POST | /search/statistics | searchAssetStatistics | :red_square: |
| GET | /search/suggestions | getSearchSuggestions | :red_square: |

</details>


<details>
<summary>Server</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /server/about | getAboutInfo | :red_square: |
| GET | /server/apk-links | getApkLinks | :red_square: |
| GET | /server/config | getServerConfig | :orange_square: <sup>2</sup> |
| GET | /server/features | getServerFeatures | :orange_square: <sup>2</sup> |
| GET | /server/license | getServerLicense | :red_square: |
| PUT | /server/license | setServerLicense | :red_square: |
| DELETE | /server/license | deleteServerLicense | :red_square: |
| GET | /server/media-types | getSupportedMediaTypes | :red_square: |
| GET | /server/ping | pingServer | :green_square: |
| GET | /server/statistics | getServerStatistics | :red_square: |
| GET | /server/storage | getStorage | :green_square: |
| GET | /server/theme | getTheme | :red_square: |
| GET | /server/version | getServerVersion | :green_square: |
| GET | /server/version-check | getVersionCheck | :red_square: |
| GET | /server/version-history | getVersionHistory | :red_square: |

</details>


<details>
<summary>Sessions</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /sessions | getSessions | :red_square: |
| POST | /sessions | createSession | :red_square: |
| DELETE | /sessions | deleteAllSessions | :red_square: |
| PUT | /sessions/{id} | updateSession | :red_square: |
| DELETE | /sessions/{id} | deleteSession | :red_square: |
| POST | /sessions/{id}/lock | lockSession | :red_square: |
</details>


<details>
<summary>Shared links</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /shared-links | getAllSharedLinks | :red_square: |
| POST | /shared-links | createSharedLink | :red_square: |
| POST | /shared-links/login | sharedLinkLogin | :red_square: |
| GET | /shared-links/me | getMySharedLink | :red_square: |
| GET | /shared-links/{id} | getSharedLinkById | :red_square: |
| DELETE | /shared-links/{id} | removeSharedLink | :red_square: |
| PATCH | /shared-links/{id} | updateSharedLink | :red_square: |
| PUT | /shared-links/{id}/assets | addSharedLinkAssets | :red_square: |
| DELETE | /shared-links/{id}/assets | removeSharedLinkAssets | :red_square: |

</details>


<details>
<summary>Stacks</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /stacks | searchStacks | :red_square: |
| POST | /stacks | createStack | :red_square: |
| DELETE | /stacks | deleteStacks | :red_square: |
| GET | /stacks/{id} | getStack | :red_square: |
| PUT | /stacks/{id} | updateStack | :red_square: |
| DELETE | /stacks/{id} | deleteStack | :red_square: |
| DELETE | /stacks/{id}/assets/{assetId} | removeAssetFromStack | :red_square: |

</details>


<details>
<summary>Sync</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /sync/ack | getSyncAck | :green_square: |
| POST | /sync/ack | sendSyncAck | :green_square: |
| DELETE | /sync/ack | deleteSyncAck | :green_square: |
| POST | /sync/stream | getSyncStream | :orange_square: <sup>4</sup>|

</details>


<details>
<summary>System config</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /system-config | getConfig | :red_square: |
| PUT | /system-config | updateConfig | :red_square: |
| GET | /system-config/defaults | getConfigDefaults | :red_square: |
| GET | /system-config/storage-template-options | getStorageTemplateOptions | :red_square: |

</details>


<details>
<summary>System metadata</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /system-metadata/admin-onboarding | getAdminOnboarding | :red_square: |
| POST | /system-metadata/admin-onboarding | updateAdminOnboarding | :red_square: |
| GET | /system-metadata/reverse-geocoding-state | getReverseGeocodingState | :red_square: |
| GET | /system-metadata/version-check-state | getVersionCheckState | :red_square: |

</details>


<details>
<summary>Tags</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /tags | getAllTags | :red_square: |
| PUT | /tags | upsertTags | :red_square: |
| POST | /tags | createTag | :red_square: |
| PUT | /tags/assets | bulkTagAssets | :red_square: |
| GET | /tags/{id} | getTagById | :red_square: |
| PUT | /tags/{id} | updateTag | :red_square: |
| DELETE | /tags/{id} | deleteTag | :red_square: |
| PUT | /tags/{id}/assets | tagAssets | :red_square: |
| DELETE | /tags/{id}/assets | untagAssets | :red_square: |

</details>


<details>
<summary>Timeline</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /timeline/bucket | getTimeBucket | :red_square: |
| GET | /timeline/buckets | getTimeBuckets | :red_square: |

</details>


<details>
<summary>Trash</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| POST | /trash/empty | emptyTrash | :red_square: |
| POST | /trash/restore | restoreTrash | :red_square: |
| POST | /trash/restore/assets | restoreAssets | :red_square: |

</details>


<details>
<summary>Users</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /users | searchUsers | :red_square: |
| GET | /users/me | getMyUser | :yellow_square: <sup>1</sup> |
| PUT | /users/me | updateMyUser | :red_square: |
| GET | /users/me/license | getUserLicense | :red_square: |
| PUT | /users/me/license | setUserLicense | :red_square: |
| DELETE | /users/me/license | deleteUserLicense | :red_square: |
| GET | /users/me/onboarding | getUserOnboarding | :red_square: |
| PUT | /users/me/onboarding | setUserOnboarding | :red_square: |
| DELETE | /users/me/onboarding | deleteUserOnboarding | :red_square: |
| GET | /users/me/preferences | getMyPreferences | :orange_square: <sup>2</sup>|
| PUT | /users/me/preferences | updateMyPreferences | :red_square: |
| POST | /users/profile-image | createProfileImage | :red_square: |
| DELETE | /users/profile-image | deleteProfileImage | :red_square: |
| GET | /users/{id} | getUser | :red_square: |
| GET | /users/{id}/profile-image | getProfileImage | :red_square: |

</details>


<details>
<summary>Users (admin)</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /admin/users | searchUsersAdmin | :red_square: |
| POST | /admin/users | createUserAdmin | :red_square: |
| GET | /admin/users/{id} | getUserAdmin | :red_square: |
| PUT | /admin/users/{id} | updateUserAdmin | :red_square: |
| DELETE | /admin/users/{id} | deleteUserAdmin | :red_square: |
| GET | /admin/users/{id}/preferences | getUserPreferencesAdmin | :red_square: |
| PUT | /admin/users/{id}/preferences | updateUserPreferencesAdmin | :red_square: |
| POST | /admin/users/{id}/restore | restoreUserAdmin | :red_square: |
| GET | /admin/users/{id}/sessions | getUserSessionsAdmin | :red_square: |
| GET | /admin/users/{id}/statistics | getUserStatisticsAdmin | :red_square: |

</details>


<details>
<summary>Views</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /view/folder | getAssetsByOriginalPath | :red_square: |
| GET | /view/folder/unique-paths | getUniqueOriginalPaths | :red_square: |

</details>


<details>
<summary>Workflows</summary>

| Method | Path | Endpoint Name | State |
|--------|------|---------------|-------|
| GET | /workflows | getWorkflows | :red_square: |
| POST | /workflows | createWorkflow | :red_square: |
| GET | /workflows/{id} | getWorkflow | :red_square: |
| PUT | /workflows/{id} | updateWorkflow | :red_square: |
| DELETE | /workflows/{id} | deleteWorkflow | :red_square: |

</details>

¹ Contains hard-coded values, but shouldn't affect usage

² Contains hard-coded values, and may affect usage

³ Implementation is incomplete, but shoudn't affect usage

⁴ Implementation is incomplete, and may affect usage