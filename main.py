# This function is automatically called by the macros plugin
def define_env(env):
    # A variable to hold the requirement counter
    env.variables["req_counter"] = 0
    env.variables["table_counter"] = 0
    env.variables["table_refs"] = {}

    @env.macro
    def requirement():
        """
        Increments the counter and returns a formatted unique requirement ID.
        """
        env.variables["req_counter"] += 1
        counter_value = env.variables["req_counter"]

        # The :03d formats the number to have at least 3 digits with leading zeros
        # Add ** to make the output bold in Markdown
        return f"**[UEC-{counter_value:03d}]**"

    @env.macro
    def table_caption(label, text):
        """
        Creates a numbered caption and stores its number for later reference.
        - label: A unique identifier for the table (e.g., 'conn_lock_fail').
        - text: The caption text to display.
        """
        env.variables["table_counter"] += 1
        number = env.variables["table_counter"]
        env.variables["table_refs"][label] = number
        return f"Table: {text}"

    # Macro to reference a table by its label
    @env.macro
    def table_ref(label):
        """
        Returns the number of a table by its label.
        """
        number = env.variables["table_refs"].get(label, "??")
        return f"Table {number}"
