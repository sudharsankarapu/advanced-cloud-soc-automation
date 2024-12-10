from google.cloud import securitycenter_v1

# Initialize Security Center client
client = securitycenter_v1.SecurityCenterClient()
org_id = "organizations/123456789"

# Fetch findings
response = client.list_findings(request={"parent": f"{org_id}/sources/-"})

# Analyze findings
for finding in response:
    if finding.finding.category == "NETWORK":
        print(f"Potential Network Issue: {finding.name}")
