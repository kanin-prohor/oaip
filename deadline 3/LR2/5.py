def filter_logs(log_lst, keyword):
    for log in log_lst:
        if keyword in log:
            yield log

logs = [
    "INFO: User 'alice' logged in",
    "ERROR: Failed to connect to database",
    "WARNING: Disk space low",
    "INFO: User 'bob' logged in",
    "ERROR: Invalid credentials",
    "DEBUG: Starting server",
]

print("ERROR лог:")
for error_log in filter_logs(logs, "ERROR"):
    print(f"  - {error_log}")

print("\nINFO лог:")
for info_log in filter_logs(logs, "INFO"):
    print(f"  - {info_log}")

error_list = list(filter_logs(logs, "ERROR"))
print(f"\nВсе ошибки: {error_list}")