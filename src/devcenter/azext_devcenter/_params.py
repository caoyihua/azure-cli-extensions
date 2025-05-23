# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=unused-import
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    get_enum_type,
    get_three_state_flag,
)
from azure.cli.core.commands.validators import (
    validate_file_or_dict,
)

from ._validators import validate_dev_box_list, validate_time, is_iso8601


dev_center_type = CLIArgumentType(
    options_list=["--dev-center-name", "--dev-center", "-d"],
    help="The name of the dev center. Use `az configure -d dev-center=<dev_center_name>` to configure a default.",
    configured_default="dev-center",
)

project_type = CLIArgumentType(
    options_list=["--project", "--project-name"],
    help="The name of the project. Use `az configure -d project=<project_name>` to configure a default.",
    configured_default="project",
)

endpoint = CLIArgumentType(
    options_list=["--endpoint"],
    help="The API endpoint for the developer resources. Use `az configure -d endpoint=<endpoint_uri>` to configure a default.",
    configured_default="endpoint",
)


def load_arguments(self, _):
    with self.argument_context("devcenter dev project list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )

    with self.argument_context("devcenter dev project show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "project_name",
            options_list=["--name", "-n"],
            type=str,
            help="The dev center " "project upon which to execute operations.",
        )

    with self.argument_context("devcenter dev project show-operation") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "project_name",
            options_list=["--name", "-n"],
            type=str,
            help="The dev center " "project upon which to execute operations.",
        )
        c.argument(
            "operation_id",
            type=str,
            help="The id of the operation on a project.",
        )

    with self.argument_context("devcenter dev project list-abilities") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "project_name",
            options_list=["--name", "-n"],
            type=str,
            help="The dev center " "project upon which to execute operations.",
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )

    with self.argument_context("devcenter dev pool list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )

    with self.argument_context("devcenter dev pool show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "pool_name",
            options_list=["--name", "-n", "--pool-name"],
            type=str,
            help="The name of a pool of " "dev boxes.",
        )

    with self.argument_context("devcenter dev schedule list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "pool_name",
            options_list=["--pool-name", "--pool"],
            type=str,
            help="The name of a pool of dev boxes.",
        )

    with self.argument_context("devcenter dev schedule show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "pool_name",
            options_list=["--pool-name", "--pool"],
            type=str,
            help="The name of a pool of dev boxes.",
        )

    with self.argument_context(
        "devcenter dev dev-box list", validator=validate_dev_box_list
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )

    with self.argument_context("devcenter dev dev-box show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box create") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "pool_name",
            options_list=["--pool-name", "--pool"],
            type=str,
            help="The name of the dev box pool this machine belongs to.",
        )

    with self.argument_context("devcenter dev dev-box delete") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box start") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box align") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box approve") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box set-active-hours") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "end_time_hour",
            options_list=["--end-time-hour"],
            type=int,
            help="The end time of the active hours.",
        )
        c.argument(
            "start_time_hour",
            options_list=["--start-time-hour"],
            type=int,
            help="The start time of the active hours.",
        )
        c.argument(
            "time_zone",
            options_list=["--time-zone"],
            type=str,
            help="The timezone of the active hours.",
        )

    with self.argument_context("devcenter dev dev-box stop") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "hibernate",
            arg_type=get_three_state_flag(),
            help="Optional parameter to hibernate the dev box.",
        )

    with self.argument_context("devcenter dev dev-box restart") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box repair") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box show-remote-connection") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box list-action") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box show-action") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "action_name",
            type=str,
            help="The name of an action that will take place on a dev box.",
        )

    with self.argument_context("devcenter dev dev-box skip-action") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "action_name",
            type=str,
            help="The name of an action that will take place on a dev box.",
        )

    with self.argument_context(
        "devcenter dev dev-box delay-action", validator=validate_time
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "action_name",
            type=str,
            help="The name of an action that will take place on a dev box.",
        )
        c.argument(
            "delay_time",
            help="The delayed timespan from the scheduled action time. Format HH:MM",
        )

    with self.argument_context(
        "devcenter dev dev-box delay-all-actions", validator=validate_time
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "delay_time",
            help="The delayed timespan from the earliest scheduled time of all actions. Format HH:MM",
        )

    with self.argument_context("devcenter dev dev-box list-operation") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box show-operation") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "operation_id",
            type=str,
            help="The id of the operation on a dev box.",
        )

    with self.argument_context("devcenter dev dev-box capture-snapshot") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev dev-box restore-snapshot") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "snapshot_id",
            options_list=["--snapshot-id", "-s"],
            type=str,
            help="Required parameter that specifies the snapshot id to use for the restore operation.",
        )

    with self.argument_context("devcenter dev dev-box show-snapshot") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )
        c.argument(
            "snapshot_id",
            options_list=["--snapshot-id", "-s"],
            type=str,
            help="Required parameter that specifies the snapshot id to use for the restore operation.",
        )

    with self.argument_context("devcenter dev dev-box list-snapshot") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--name", "-n", "--dev-box-name"],
            type=str,
            help="The name of a dev " "box.",
        )

    with self.argument_context("devcenter dev environment list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )

    with self.argument_context("devcenter dev environment show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )

    with self.argument_context(
        "devcenter dev environment create", validator=is_iso8601
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "parameters",
            type=validate_file_or_dict,
            help="Parameters object for the environment. Expected "
            "value: json-string/json-file/@json-file.",
        )
        c.argument("environment_type", type=str, help="Environment type.")
        c.argument("catalog_name", type=str, help="Name of the catalog.")
        c.argument(
            "environment_definition_name",
            options_list=["-e", "--environment-definition-name"],
            type=str,
            help="Name of the environment definition.",
        )
        c.argument(
            "expiration_date",
            options_list=["--expiration-date", "--expiration"],
            type=str,
            help="The time the expiration date will be triggered (UTC), after which the environment"
            " and associated resources will be deleted. The string format is ISO format.",
        )

    with self.argument_context(
        "devcenter dev environment update", validator=is_iso8601
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "parameters",
            type=validate_file_or_dict,
            help="Parameters object for the environment. Expected "
            "value: json-string/json-file/@json-file.",
        )
        c.argument(
            "expiration_date",
            options_list=["--expiration-date", "--expiration"],
            type=str,
            help="The date of environment expiration. Must be an ISO string",
        )

    with self.argument_context(
        "devcenter dev environment deploy", validator=is_iso8601
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "parameters",
            type=validate_file_or_dict,
            help="Parameters object for the environment. Expected "
            "value: json-string/json-file/@json-file.",
        )
        c.argument(
            "expiration_date",
            options_list=["--expiration-date", "--expiration"],
            type=str,
            help="The date of environment expiration. Must be an ISO string",
        )

    with self.argument_context("devcenter dev environment delete") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "force",
            arg_type=get_three_state_flag(),
            help="Optional to force environment deletion even if the environment definition does not exist. "
            "This is a best-effort delete, and anything custom that forces resource creation beyond the associated resource group may not be deleted.",
        )

    with self.argument_context("devcenter dev catalog list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )

    with self.argument_context("devcenter dev catalog show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "catalog_name",
            options_list=["--name", "-n", "--catalog-name"],
            type=str,
            help="The name of the catalog",
        )

    with self.argument_context("devcenter dev environment-definition list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            required=True,
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument("catalog_name", type=str, help="The name of the catalog")

    with self.argument_context("devcenter dev environment-definition show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            required=True,
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument("catalog_name", type=str, help="The name of the catalog")
        c.argument(
            "definition_name",
            options_list=["--name", "-n", "--definition-name"],
            type=str,
            help="The name of the environment definition",
        )

    with self.argument_context("devcenter dev environment-type list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )

    with self.argument_context("devcenter dev environment-type show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument("environment_type_name", options_list=[
                   "-n", "--name", "--environment-type-name"], type=str, help="Environment type.")

    with self.argument_context("devcenter dev environment-type list-abilities") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument("environment_type_name", options_list=[
                   "-n", "--name", "--environment-type-name"], type=str, help="Environment type.")
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )

    with self.argument_context("devcenter dev image-build show-log") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument("image_build_log_id", options_list=[
                   "-i", "--image-build-log-id"], type=str, help="An imaging build log id.")

    with self.argument_context("devcenter dev environment list-operation") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )

    with self.argument_context("devcenter dev environment show-operation") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "operation_id",
            options_list=["--operation-id"],
            type=str,
            help="The ID " "of the operation.",
        )

    with self.argument_context("devcenter dev environment show-logs-by-operation") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "operation_id",
            options_list=["--operation-id"],
            type=str,
            help="The ID " "of the operation.",
        )

    with self.argument_context("devcenter dev environment show-action") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "action_name",
            options_list=["--action-name"],
            type=str,
            help="The name of an action that will take place on an environment.",
        )

    with self.argument_context("devcenter dev environment skip-action") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "action_name",
            options_list=["--action-name"],
            type=str,
            help="The name of an action that will take place on an environment.",
        )

    with self.argument_context("devcenter dev environment list-action") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )

    with self.argument_context(
        "devcenter dev environment delay-action", validator=validate_time
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "action_name",
            options_list=["--action-name"],
            type=str,
            help="The name of an action that will take place on an environment.",
        )
        c.argument(
            "delay_time",
            help="The delayed timespan from the scheduled action time. Format HH:MM",
        )

    with self.argument_context("devcenter dev environment show-outputs") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )

    with self.argument_context(
        "devcenter dev environment update-expiration-date", validator=is_iso8601
    ) as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken from the "
            "authentication context",
        )
        c.argument(
            "environment_name",
            options_list=["--name", "-n", "--environment-name"],
            type=str,
            help="The name " "of the environment.",
        )
        c.argument(
            "expiration_date",
            options_list=["--expiration-date", "--expiration"],
            type=str,
            help="The time the expiration date will be triggered (UTC), after which the environment "
            "and associated resources will be deleted. The string format is ISO format.",
        )

    with self.argument_context("devcenter dev customization-group create") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "tasks",
            type=validate_file_or_dict,
            help="Parameters object for the tasks. Expected "
            "value: json-string/json-file/@json-file.",
        )
        c.argument(
            "customization_group_name",
            options_list=["--name", "-n", "--customization-group-name"],
            type=str,
            help="The name of customization group",
        )

    with self.argument_context("devcenter dev customization-group show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "customization_group_name",
            options_list=["--name", "-n", "--customization-group-name"],
            type=str,
            help="The name of customization group",
        )

    with self.argument_context("devcenter dev customization-group list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "include_tasks",
            arg_type=get_three_state_flag(),
            help="Optional parameter to include task information in the response.",
        )

    with self.argument_context("devcenter dev customization-task show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument("catalog_name", type=str, help="The name of the catalog")
        c.argument("task_name", options_list=["-n", "--name", "--task-name"],
                   type=str, help="The name of the task")

    with self.argument_context("devcenter dev customization-task list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )

    with self.argument_context("devcenter dev customization-task validate") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "tasks",
            type=validate_file_or_dict,
            help="Parameters object for the tasks. Expected "
            "value: json-string/json-file/@json-file.",
        )

    with self.argument_context("devcenter dev customization-task show-logs") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "customization_task_id",
            options_list=["--customization-task-id", "--task-id" "-t"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "customization_group_name",
            options_list=["--name", "-n", "--customization-group-name"],
            type=str,
            help="The name of customization group",
        )

    with self.argument_context("devcenter dev approval list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )

    with self.argument_context("devcenter dev add-on disable") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "add_on_name",
            options_list=["-n", "--name", "--add-on-name"],
            type=str,
            help="The name of dev box add on",
        )

    with self.argument_context("devcenter dev add-on create") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "add_on_name",
            options_list=["-n", "--name", "--add-on-name"],
            type=str,
            help="The name of dev box add on",
        )
        c.argument(
            "hosting_resource_name",
            options_list=["--hosting-resource-name"],
            type=str,
            help="The hosting resource name, either a DevBox or HyperV.  Leaving it empty or `Default` if it's for DevBox.",
        )

    with self.argument_context("devcenter dev add-on delete") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "add_on_name",
            options_list=["-n", "--name", "--add-on-name"],
            type=str,
            help="The name of dev box add on",
        )

    with self.argument_context("devcenter dev add-on disable") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "add_on_name",
            options_list=["-n", "--name", "--add-on-name"],
            type=str,
            help="The name of dev box add on",
        )

    with self.argument_context("devcenter dev add-on enable") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "add_on_name",
            options_list=["-n", "--name", "--add-on-name"],
            type=str,
            help="The name of dev box add on",
        )

    with self.argument_context("devcenter dev add-on show") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
        c.argument(
            "add_on_name",
            options_list=["-n", "--name", "--add-on-name"],
            type=str,
            help="The name of dev box add on",
        )

    with self.argument_context("devcenter dev add-on list") as c:
        c.argument(
            "dev_center",
            arg_type=dev_center_type,
        )
        c.argument(
            "project_name",
            arg_type=project_type,
        )
        c.argument(
            "endpoint",
            arg_type=endpoint,
        )
        c.argument(
            "user_id",
            type=str,
            help="The AAD object id of the user. If value is 'me', the identity is taken "
            "from the authentication context.",
        )
        c.argument(
            "dev_box_name",
            options_list=["--dev-box-name", "--dev-box"],
            type=str,
            help="The name " "of the dev box.",
        )
