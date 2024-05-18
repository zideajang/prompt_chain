

def get_initial_boot_messages(version="startup"):
    if version == "startup":
        initial_boot_message = INITIAL_BOOT_MESSAGE
        messages = [
            {"role": "assistant", "content": initial_boot_message},
        ]