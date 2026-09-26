"""
One time setup for setting the required scopes and secrets for the project

usage:
    python setup_secrets.py
"""

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace
import getpass

workspace_client = WorkspaceClient()

# Create Massive API Scope and secrets
workspace_client.secrets.create_scope(scope="massive")
workspace_client.secrets.put_secret(
    scope="massive",
    key="massive_api_key",
    string_value=getpass.getpass("Enter Massive API Key:"),
)

# Create Lakebse database Scope and secrets
workspace_client.secrets.create_scope(scope="lakebase")
workspace_client.secrets.put_secret(
    scope="lakebase",
    key="lakebase_connection_string",
    string_value=getpass.getpass("Enter Lakebase Connection String:"),
)

# Manage access control list
workspace_client.secrets.put_acl(
    scope="massive", principal="users", permission=workspace.AclPermission.READ
)
workspace_client.secrets.put_acl(
    scope="lakebase", principal="users", permission=workspace.AclPermission.READ
)
