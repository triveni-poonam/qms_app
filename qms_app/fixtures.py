import frappe

def get_all_fixtures():
    """Dynamically fetch all DocTypes and related metadata for export."""
    app_name = "qms_app"  # Change this to your actual app name

    # Fetch all DocTypes that belong to this app
    doctypes = frappe.get_all("DocType", filters={"module": ["like", f"%{app_name}%"]}, pluck="name")

    # Additional standard fixtures that should always be exported
    additional_fixtures = [
        "Custom Field",
        "Property Setter",
        "Client Script",
        "Server Script",
        "Report",
        "Print Format",
        "Page",
        "Role",
        "Notification",
        "Email Template",
        "Dashboard",
        "Dashboard Chart",
        "Workspace",
        "Website Settings"
    ]

    # Combine detected DocTypes and standard fixtures
    return [{"dt": dt} for dt in doctypes + additional_fixtures]

# Make this available as `fixtures` for Frappe
fixtures = get_all_fixtures()
