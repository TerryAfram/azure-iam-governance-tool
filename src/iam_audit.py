import subprocess
import json
from datetime import datetime, timedelta

cmd = "az role assignment list --include-inherited --query \"[*].{name:principalName, id:principalId, role:roleDefinitionName}\" --output json"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

if result.returncode == 0:
    data = json.loads(result.stdout)
    print(f"Successfully retrieved {len(data)} total assignments.")

    for identity in data:
        display_name = identity.get('name') if identity.get('name') else f"ID: {identity['id']}"
        user_id = identity['id']
        
        check_cmd = f"az ad user show --id {user_id} --query 'signInActivity.lastSignInDateTime' --output tsv"
        signin_result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)

        if signin_result.stdout.strip():
            last_signin = datetime.fromisoformat(signin_result.stdout.strip().replace('Z', ''))
            threshold = datetime.now() - timedelta(days=90)
            
            if last_signin < threshold:
                print(f"FLAGGED: {display_name} (Last sign-in: {last_signin.date()})")
        else:
            print(f"FLAGGED: {display_name} (No sign-in activity found)")
else:
    print(f"Error executing command: {result.stderr}")
