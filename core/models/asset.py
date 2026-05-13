from core.enums.asset_status import AssetStatus
from core.enums.asset_type import AssetType
from core.enums.asset_visibility import AssetVisibility
from core.enums.checksum_algorithm import ChecksumAlgorithm
from core.models.user import User
from core.models.library import Library
from core.models.stack import Stack
from core.utils.split_uuid import split_uuid
from django.db import models
import uuid

def asset_file_path(instance, filename):
    return f'upload/{str(instance.owner.id)}/{split_uuid(instance.id)}.{filename.split('.')[-1]}'


class Asset(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )
    # TODO: missing on_update cascade?
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=64,
        choices=AssetType,
    )
    original = models.FileField(upload_to=asset_file_path)
    file_created_at = models.DateTimeField()
    file_modified_at = models.DateTimeField()
    is_favorite = models.BooleanField(default=False)
    duration = models.IntegerField(
        blank=True,
        null=True,
    )
    checksum = models.BinaryField()
    checksum_algorithm = models.CharField(
        max_length=64,
        choices=ChecksumAlgorithm,
    )
    # TODO: missing on_update cascade?
    live_photo_video_id = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    original_file_name = models.CharField(max_length=255)
    thumbhash = models.BinaryField(
        blank=True,
        null=True,
    )
    is_offline = models.BooleanField(default=False)
    # TODO: missing on_update cascade?
    library_id = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        null=True,
    )
    is_external = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    local_date_time = models.DateTimeField()
    stack_id = models.ForeignKey(
        Stack,
        on_delete=models.SET_NULL,
        null=True,
    )
    duplicate_id = models.UUIDField(
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=255,
        choices=AssetStatus,
        default=AssetStatus.ACTIVE,
    )
    update_id = models.UUIDField(default=uuid.uuid7)
    visibility = models.CharField(
        max_length=255,
        choices=AssetVisibility,
        default=AssetVisibility.TIMELINE,
    )
    width = models.IntegerField()
    height = models.IntegerField()
    is_edited = models.BooleanField(default=True)


    class Meta:
        # TODO: Are these all?
        indexes = [
            models.Index(fields=['file_created_at']),
            models.Index(fields=['checksum']),
            models.Index(fields=['original_file_name']),
            models.Index(fields=['duplicate_id']),
            models.Index(fields=['update_id']),
            models.Index(fields=['id']),
            models.Index(
                fields=[
                    'owner',
                    'checksum',
                ]
            ),
            models.Index(
                fields=[
                    'owner',
                    'library_id',
                    'checksum',
                ]
            ),
            models.Index(
                fields=[
                    'original',
                    'library_id',
                ]
            ),
            models.Index(
                fields=[
                    'id',
                    'stack_id',
                ]
            ),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'owner',
                    'checksum',
                ],
                name='unique_asset_checksum',
            ),
            models.UniqueConstraint(
                fields=[
                    'owner',
                    'library_id',
                    'checksum',
                ],
                name='unique_asset_checksum_library_id',
            )
        ]

    def save(self, *args, **kwargs):
        self.update_id = uuid.uuid7()
        super().save(*args, **kwargs)
