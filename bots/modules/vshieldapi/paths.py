_PATHS = {
    "system":
        {
            "GET_PLANS": "/system/getplans",
            "GET_PENDING_ORDERS": "/system/getPendingOrders",
            "GET_TASK_INFO": "/system/getTaskInfo/{task}"
        },
    "service":
        {
            "GET_SERVICES": "/service/getList",
            "GET_SERVICE_INFO": "/service/getInfo/{service}",
            "CREATE_SERVICE_TASK": "/service/createTask/{service}",
            "MANAGE_AUTO_RENEW": "/service/manageAutoRenew/{service}",
            "RENEW_SERVICE": "/service/renew/{service}"
        },
    "server":
        {
            "GET_SERVERS": "/server/getList",
            "GET_SERVER_INFO": "/server/getInfo/{server}",
            "GET_GRAPHS": "/server/getGraphs/{server}",
            "GET_CONSOLE": "/server/Console/{server}",
            "CREATE_TASK": "/server/createTask/{server}",
            "MANAGE_AUTO_RENEW": "/server/manageAutoRenew/{server}",
            "UPDATE_HOSTNAME": "/server/updateHostname/{server}",
            "UPGRADE": "/server/upgrade/{server}",
            "CHANGE_IP": "/server/changeIp/{server}",
            "RENEW": "/server/renew/{server}",
            "DELETE": "/server/delete/{server}",
            "ORDER": "/server/order"
        },
    "billing":
        {
            "BALANCE": "/billing/getBalance",
            "TRANSACTIONS": "/billing/getTransactions",
            "INVOICES": "/billing/getInvoices",
            "INVOICE_INFO": "/billing/getInvoicesInfo/{invoice}",
        },
    "firewall":
        {
            "INFO": "/firewall/getInfo/{service}"
        }
}