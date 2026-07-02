#https://mixpanel.github.io/mixpanel-headless/getting-started/installation/
# #project credentials here

import mixpanel_headless as mp

ws = mp.Workspace()

# Insights
ws.query("Login")                           

# ws.query_funnel(["Signup", "Purchase"])      # Funnels
# ws.query_retention("Signup", "Login")        # Retention
# ws.query_flow("Purchase")                    # Flows
# ws.query_user(where=Filter.is_set("$email")) # Users
# 