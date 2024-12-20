import pprint
import re  # noqa: F401

import six
from omagent_core.engine.http.models.task_result_status import TaskResultStatus


class TaskResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "workflow_instance_id": "str",
        "task_id": "str",
        "reason_for_incompletion": "str",
        "callback_after_seconds": "int",
        "worker_id": "str",
        "status": "str",
        "output_data": "dict(str, object)",
        "logs": "list[TaskExecLog]",
        "external_output_payload_storage_path": "str",
        "sub_workflow_id": "str",
    }

    attribute_map = {
        "workflow_instance_id": "workflowInstanceId",
        "task_id": "taskId",
        "reason_for_incompletion": "reasonForIncompletion",
        "callback_after_seconds": "callbackAfterSeconds",
        "worker_id": "workerId",
        "status": "status",
        "output_data": "outputData",
        "logs": "logs",
        "external_output_payload_storage_path": "externalOutputPayloadStoragePath",
        "sub_workflow_id": "subWorkflowId",
    }

    def __init__(
        self,
        workflow_instance_id=None,
        task_id=None,
        reason_for_incompletion=None,
        callback_after_seconds=None,
        worker_id=None,
        status=None,
        output_data=None,
        logs=None,
        external_output_payload_storage_path=None,
        sub_workflow_id=None,
    ):  # noqa: E501
        """TaskResult - a model defined in Swagger"""  # noqa: E501
        self._workflow_instance_id = None
        self._task_id = None
        self._reason_for_incompletion = None
        self._callback_after_seconds = None
        self._worker_id = None
        self._status = None
        self._output_data = None
        self._logs = None
        self._external_output_payload_storage_path = None
        self._sub_workflow_id = None
        self.discriminator = None
        self.workflow_instance_id = workflow_instance_id
        self.task_id = task_id
        if reason_for_incompletion is not None:
            self.reason_for_incompletion = reason_for_incompletion
        if callback_after_seconds is not None:
            self.callback_after_seconds = callback_after_seconds
        if worker_id is not None:
            self.worker_id = worker_id
        if status is not None:
            self.status = status
        if output_data is not None:
            self.output_data = output_data
        if logs is not None:
            self.logs = logs
        if external_output_payload_storage_path is not None:
            self.external_output_payload_storage_path = (
                external_output_payload_storage_path
            )
        if sub_workflow_id is not None:
            self.sub_workflow_id = sub_workflow_id

    @property
    def workflow_instance_id(self):
        """Gets the workflow_instance_id of this TaskResult.  # noqa: E501


        :return: The workflow_instance_id of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._workflow_instance_id

    @workflow_instance_id.setter
    def workflow_instance_id(self, workflow_instance_id):
        """Sets the workflow_instance_id of this TaskResult.


        :param workflow_instance_id: The workflow_instance_id of this TaskResult.  # noqa: E501
        :type: str
        """
        self._workflow_instance_id = workflow_instance_id

    @property
    def task_id(self):
        """Gets the task_id of this TaskResult.  # noqa: E501


        :return: The task_id of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskResult.


        :param task_id: The task_id of this TaskResult.  # noqa: E501
        :type: str
        """
        self._task_id = task_id

    @property
    def reason_for_incompletion(self):
        """Gets the reason_for_incompletion of this TaskResult.  # noqa: E501


        :return: The reason_for_incompletion of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._reason_for_incompletion

    @reason_for_incompletion.setter
    def reason_for_incompletion(self, reason_for_incompletion):
        """Sets the reason_for_incompletion of this TaskResult.


        :param reason_for_incompletion: The reason_for_incompletion of this TaskResult.  # noqa: E501
        :type: str
        """

        self._reason_for_incompletion = reason_for_incompletion

    @property
    def callback_after_seconds(self):
        """Gets the callback_after_seconds of this TaskResult.  # noqa: E501


        :return: The callback_after_seconds of this TaskResult.  # noqa: E501
        :rtype: int
        """
        return self._callback_after_seconds

    @callback_after_seconds.setter
    def callback_after_seconds(self, callback_after_seconds):
        """Sets the callback_after_seconds of this TaskResult.


        :param callback_after_seconds: The callback_after_seconds of this TaskResult.  # noqa: E501
        :type: int
        """

        self._callback_after_seconds = callback_after_seconds

    @property
    def worker_id(self):
        """Gets the worker_id of this TaskResult.  # noqa: E501


        :return: The worker_id of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._worker_id

    @worker_id.setter
    def worker_id(self, worker_id):
        """Sets the worker_id of this TaskResult.


        :param worker_id: The worker_id of this TaskResult.  # noqa: E501
        :type: str
        """

        self._worker_id = worker_id

    @property
    def status(self):
        """Gets the status of this TaskResult.  # noqa: E501


        :return: The status of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskResult.


        :param status: The status of this TaskResult.  # noqa: E501
        :type: str
        """
        allowed_values = [
            task_result_status.name for task_result_status in TaskResultStatus
        ]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = TaskResultStatus[status]

    @property
    def output_data(self):
        """Gets the output_data of this TaskResult.  # noqa: E501


        :return: The output_data of this TaskResult.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._output_data

    @output_data.setter
    def output_data(self, output_data):
        """Sets the output_data of this TaskResult.


        :param output_data: The output_data of this TaskResult.  # noqa: E501
        :type: dict(str, object)
        """

        self._output_data = output_data

    @property
    def logs(self):
        """Gets the logs of this TaskResult.  # noqa: E501


        :return: The logs of this TaskResult.  # noqa: E501
        :rtype: list[TaskExecLog]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this TaskResult.


        :param logs: The logs of this TaskResult.  # noqa: E501
        :type: list[TaskExecLog]
        """

        self._logs = logs

    @property
    def external_output_payload_storage_path(self):
        """Gets the external_output_payload_storage_path of this TaskResult.  # noqa: E501


        :return: The external_output_payload_storage_path of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._external_output_payload_storage_path

    @external_output_payload_storage_path.setter
    def external_output_payload_storage_path(
        self, external_output_payload_storage_path
    ):
        """Sets the external_output_payload_storage_path of this TaskResult.


        :param external_output_payload_storage_path: The external_output_payload_storage_path of this TaskResult.  # noqa: E501
        :type: str
        """

        self._external_output_payload_storage_path = (
            external_output_payload_storage_path
        )

    @property
    def sub_workflow_id(self):
        """Gets the sub_workflow_id of this TaskResult.  # noqa: E501


        :return: The sub_workflow_id of this TaskResult.  # noqa: E501
        :rtype: str
        """
        return self._sub_workflow_id

    @sub_workflow_id.setter
    def sub_workflow_id(self, sub_workflow_id):
        """Sets the sub_workflow_id of this TaskResult.


        :param sub_workflow_id: The sub_workflow_id of this TaskResult.  # noqa: E501
        :type: str
        """

        self._sub_workflow_id = sub_workflow_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(TaskResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    def add_output_data(self, key, value):
        if self.output_data == None:
            self.output_data = {}
        self.output_data[key] = value
