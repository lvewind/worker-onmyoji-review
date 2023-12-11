import wmi
import pythoncom


def get_network_eth_list():
    """
    获取网络适配器列表
    """
    pythoncom.CoInitialize()
    c = wmi.WMI()
    adapter_net_connection_id_list = []
    physical_adapters = c.Win32_NetworkAdapter(PhysicalAdapter=True)
    if physical_adapters:
        for obj in physical_adapters:
            adapter_net_connection_id_list.append(obj.NetConnectionID)
        return adapter_net_connection_id_list
    else:
        return []


def is_adapter_exist(net_connection_id):
    """
    适配器是否存在
    """
    pythoncom.CoInitialize()
    c = wmi.WMI()
    adapter = c.Win32_NetworkAdapter(NetConnectionID=net_connection_id)
    if adapter:
        return True
    else:
        return False


def is_adapter_enable(net_connection_id):
    """
    适配器是都启用
    """
    pythoncom.CoInitialize()
    c = wmi.WMI()
    adapters = c.Win32_NetworkAdapter(NetConnectionID=net_connection_id)
    for adapter in adapters:
        try:
            mac_address = adapter.MACAddress
            if mac_address:
                return True
            else:
                return False
        except :
            return False


def get_adapter_ipv4(net_connection_id):
    """
    获取适配器ipv4地址
    """
    pythoncom.CoInitialize()
    c = wmi.WMI()

    adapters = c.Win32_NetworkAdapter(NetConnectionID=net_connection_id)
    for adapter in adapters:
        description = adapter.Description
        if description:
            adapters_2 = c.Win32_NetworkAdapterConfiguration(Description=description)
            for adapter_2 in adapters_2:
                try:
                    return adapter_2.IPAddress[0]
                except:
                    return ""


def is_adapter_dhcp_enabled(net_connection_id):
    """
    是否开启DHCP
    """
    pythoncom.CoInitialize()
    c = wmi.WMI()
    adapters = c.Win32_NetworkAdapter(NetConnectionID=net_connection_id)
    for adapter in adapters:
        description = adapter.Description
        if description:
            adapters_2 = c.Win32_NetworkAdapterConfiguration(Description=description)
            for adapter_2 in adapters_2:
                try:
                    return adapter_2.DHCPEnabled
                except:
                    return False
