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

from google.api import distribution_pb2  # type: ignore
from google.api import metric_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.logging.v2',
    manifest={
        'LogMetric',
        'ListLogMetricsRequest',
        'ListLogMetricsResponse',
        'GetLogMetricRequest',
        'CreateLogMetricRequest',
        'UpdateLogMetricRequest',
        'DeleteLogMetricRequest',
    },
)


from .requests import (
        ListLogMetricsRequest,
        GetLogMetricRequest,
        CreateLogMetricRequest,
        UpdateLogMetricRequest,
        DeleteLogMetricRequest,
)

from .responses import (
        ListLogMetricsResponse,
)


class LogMetric(proto.Message):
    r"""Describes a logs-based metric. The value of the metric is the
    number of log entries that match a logs filter in a given time
    interval.
    Logs-based metrics can also be used to extract values from logs
    and create a distribution of the values. The distribution
    records the statistics of the extracted values along with an
    optional histogram of the values as specified by the bucket
    options.

    Attributes:
        name (str):
            Required. The client-assigned metric identifier. Examples:
            ``"error_count"``, ``"nginx/requests"``.

            Metric identifiers are limited to 100 characters and can
            include only the following characters: ``A-Z``, ``a-z``,
            ``0-9``, and the special characters ``_-.,+!*',()%/``. The
            forward-slash character (``/``) denotes a hierarchy of name
            pieces, and it cannot be the first character of the name.

            The metric identifier in this field must not be
            `URL-encoded <https://en.wikipedia.org/wiki/Percent-encoding>`__.
            However, when the metric identifier appears as the
            ``[METRIC_ID]`` part of a ``metric_name`` API parameter,
            then the metric identifier must be URL-encoded. Example:
            ``"projects/my-project/metrics/nginx%2Frequests"``.
        description (str):
            Optional. A description of this metric, which
            is used in documentation. The maximum length of
            the description is 8000 characters.
        filter (str):
            Required. An `advanced logs
            filter <https://cloud.google.com/logging/docs/view/advanced_filters>`__
            which is used to match log entries. Example:

            ::

                "resource.type=gae_app AND severity>=ERROR"

            The maximum length of the filter is 20000 characters.
        metric_descriptor (google.api.metric_pb2.MetricDescriptor):
            Optional. The metric descriptor associated with the
            logs-based metric. If unspecified, it uses a default metric
            descriptor with a DELTA metric kind, INT64 value type, with
            no labels and a unit of "1". Such a metric counts the number
            of log entries matching the ``filter`` expression.

            The ``name``, ``type``, and ``description`` fields in the
            ``metric_descriptor`` are output only, and is constructed
            using the ``name`` and ``description`` field in the
            LogMetric.

            To create a logs-based metric that records a distribution of
            log values, a DELTA metric kind with a DISTRIBUTION value
            type must be used along with a ``value_extractor``
            expression in the LogMetric.

            Each label in the metric descriptor must have a matching
            label name as the key and an extractor expression as the
            value in the ``label_extractors`` map.

            The ``metric_kind`` and ``value_type`` fields in the
            ``metric_descriptor`` cannot be updated once initially
            configured. New labels can be added in the
            ``metric_descriptor``, but existing labels cannot be
            modified except for their description.
        value_extractor (str):
            Optional. A ``value_extractor`` is required when using a
            distribution logs-based metric to extract the values to
            record from a log entry. Two functions are supported for
            value extraction: ``EXTRACT(field)`` or
            ``REGEXP_EXTRACT(field, regex)``. The argument are:

            1. field: The name of the log entry field from which the
               value is to be extracted.
            2. regex: A regular expression using the Google RE2 syntax
               (https://github.com/google/re2/wiki/Syntax) with a single
               capture group to extract data from the specified log
               entry field. The value of the field is converted to a
               string before applying the regex. It is an error to
               specify a regex that does not include exactly one capture
               group.

            The result of the extraction must be convertible to a double
            type, as the distribution always records double values. If
            either the extraction or the conversion to double fails,
            then those values are not recorded in the distribution.

            Example:
            ``REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*")``
        label_extractors (Mapping[str, str]):
            Optional. A map from a label key string to an extractor
            expression which is used to extract data from a log entry
            field and assign as the label value. Each label key
            specified in the LabelDescriptor must have an associated
            extractor expression in this map. The syntax of the
            extractor expression is the same as for the
            ``value_extractor`` field.

            The extracted value is converted to the type defined in the
            label descriptor. If the either the extraction or the type
            conversion fails, the label will have a default value. The
            default value for a string label is an empty string, for an
            integer label its 0, and for a boolean label its ``false``.

            Note that there are upper bounds on the maximum number of
            labels and the number of active time series that are allowed
            in a project.
        bucket_options (google.api.distribution_pb2.BucketOptions):
            Optional. The ``bucket_options`` are required when the
            logs-based metric is using a DISTRIBUTION value type and it
            describes the bucket boundaries used to create a histogram
            of the extracted values.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of the
            metric.
            This field may not be present for older metrics.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            metric.
            This field may not be present for older metrics.
        version (google.cloud.logging_v2.types.LogMetric.ApiVersion):
            Deprecated. The API version that created or
            updated this metric. The v2 format is used by
            default and cannot be changed.
    """
    class ApiVersion(proto.Enum):
        r"""Logging API version."""
        V2 = 0
        V1 = 1

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    description = proto.Field(
        proto.STRING,
        number=2,
    )
    filter = proto.Field(
        proto.STRING,
        number=3,
    )
    metric_descriptor = proto.Field(
        proto.MESSAGE,
        number=5,
        message=metric_pb2.MetricDescriptor,
    )
    value_extractor = proto.Field(
        proto.STRING,
        number=6,
    )
    label_extractors = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    bucket_options = proto.Field(
        proto.MESSAGE,
        number=8,
        message=distribution_pb2.Distribution.BucketOptions,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    version = proto.Field(
        proto.ENUM,
        number=4,
        enum=ApiVersion,
    )


__all__ = tuple(sorted(__protobuf__.manifest))