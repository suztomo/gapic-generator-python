# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.eventarc_v1.types import trigger as gce_trigger
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.eventarc.v1',
    manifest={
        'GetTriggerRequest',
        'ListTriggersRequest',
        'ListTriggersResponse',
        'CreateTriggerRequest',
        'UpdateTriggerRequest',
        'DeleteTriggerRequest',
        'OperationMetadata',
    },
)


from .requests import (
        GetTriggerRequest,
        ListTriggersRequest,
        CreateTriggerRequest,
        UpdateTriggerRequest,
        DeleteTriggerRequest,
)

from .responses import (
        ListTriggersResponse,
)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target = proto.Field(
        proto.STRING,
        number=3,
    )
    verb = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version = proto.Field(
        proto.STRING,
        number=7,
    )


#class _MagicProtoCompletion_google_cloud_eventarc_v1_6(proto.Message):
#    """
#    This is magic. This class needs to be here, so the Metaclass-proto-miracle-workings
#    could properly construct all the protobuf classes and pretend like if they were from
#    this file and not from other/requests/responses.py.
#    """
#    pass

__all__ = tuple(sorted(__protobuf__.manifest))
