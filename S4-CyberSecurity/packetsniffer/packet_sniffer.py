# ========================================= #
# Author: Luke Hendriks
# OS: Use this program on a Linux OS!

# Imports
import pyfiglet
import socket
import struct
import binascii
import re
import ipaddress
import time

# Globals
wanted_protocol = ""
advanced = False


# Color Class to use throughout the code.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Protocol Headers
class protocolHeaders:
    TCP = 6
    UDP = 17
    ICMP = 1
    ROUTING = 43
    ICMPV6 = 58
    FRAGMENT = 44
    HOPOPT = 0
    DESTINATION = 60
    AUTHENTICATING = 51
    ENCAPSULING = 50


# TCP Flags
class tcpv6Flag:
    URGENT = 32
    ACKNOWLEDGE = 16
    PUSHFLAG = 8
    RESETFLAG = 4
    SYNFLAG = 2


# Start Print Packet Sniffer in ASCII Render
def start():
    title = pyfiglet.figlet_format("Packet Sniffer")
    print(title)
    print("Welcome to my Packet Sniffer!\n")
    print("Info: ")
    print("     - Press ctrl+c while sniffing to go back to the menu")
    print("     - If Advanced mode is enabled, you will get more details about a packet that is sniffed")
    print("")
    cli_menu()


# Cli Menu with questions, f.e. advanced mode
def cli_menu():
    # Get the IP version that will be used
    def ip_version(protocol):
        IPvX = input("Which IP Version do you want IPv4 of IPv6? ")
        IPvXUpper = IPvX.upper()

        if IPvXUpper == "IPV4":
            print("\n" + color.BOLD + "You chose: " + color.END + wanted_protocol + " - " + IPvXUpper)
            if advanced:
                print(color.BOLD + "Advanced mode is set to: " + color.END + "True")
            if not advanced:
                print(color.BOLD + "Advanced mode is set to: " + color.END + "False")
            print(20 * "=" + "Starting Sniffer" + 20 * "=" + "\n")
            time.sleep(3)
            sniffer(wanted_protocol, IPvXUpper)

        elif IPvXUpper == "IPV6":
            print("\n" + color.BOLD + "You chose: " + color.END + wanted_protocol + " - " + IPvXUpper)
            if advanced:
                print(color.BOLD + "Advanced mode is set to: " + color.END + "True")
            if not advanced:
                print(color.BOLD + "Advanced mode is set to: " + color.END + "False")
            print(20 * "=" + "Starting Sniffer" + 20 * "=")
            sniffer(wanted_protocol, IPvXUpper)

        else:
            print(color.BOLD + "Please enter a valid version! Supported verions are IPv4 and IPv6!" + color.END + "\n")
            ip_version(protocol)

    # Get the protocol that will be sniffed
    def protocol_input():
        print("Please select a protocol:\n - ICMP\n - UDP\n - TCP")
        global wanted_protocol
        protocol = input()
        protocolUpper = protocol.upper()
        wanted_protocol = protocolUpper
        if protocolUpper == "ICMP":
            ip_version(protocolUpper)
        elif protocolUpper == "TCP":
            ip_version(protocolUpper)
        elif protocolUpper == "UDP":
            ip_version(protocolUpper)
        else:
            print(color.BOLD + "Please enter a valid protocol! Supported protocols are ICMP, UDP and TCP!" + color.END
                  + "\n")
            protocol_input()

    # Advanced mode on or off
    def advanced():
        global advanced
        user_advanced = input("Do you want to enable advanced mode? y/N ")
        if user_advanced.upper() == "Y":
            advanced = True
            protocol_input()
        else:
            advanced = False
            protocol_input()

    advanced()


###########################################################################
# ============================ FORMAT STRING ============================ #
###########################################################################
# Format MAC Address
def mac_format(raw_mac):
    decoded_mac = raw_mac.decode("utf-8")
    raw_mac_list = re.findall("..?", decoded_mac)
    format_mac_address = ":".join(raw_mac_list)
    return format_mac_address


# Format IP Address
def ip_format(proto, raw_ip):
    if proto == "IPV4":
        ip_addr = ipaddress.IPv4Address(raw_ip)
        return ip_addr
    elif proto == "IPV6":
        ip_addr = ipaddress.IPv6Address(raw_ip)
        return ip_addr


###########################################################################
# ========================= PACKET INFO GLOBAL ========================== #
###########################################################################
# Ethernet Frame Info
def ethernet_frame(data):
    proto = ""
    IpHeader = struct.unpack("!6s6sH", data[0:14])
    dstMac = binascii.hexlify(IpHeader[0])
    srcMac = binascii.hexlify(IpHeader[1])
    protoType = IpHeader[2]
    nextProto = hex(protoType)

    if nextProto == '0x800':
        proto = 'IPV4'
    elif nextProto == '0x86dd':
        proto = 'IPV6'

    data = data[14:]
    return dstMac, srcMac, proto, data


###########################################################################
# ========================= PACKET INFO IPV4 ============================ #
###########################################################################
# Extra IPv4 Packet Info
def ipv4_packet(data):
    version_header_len = data[0]
    version = version_header_len >> 4
    header_len = (version_header_len & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_len, ttl, proto, src, target, data[header_len:]


# Extra ICMP Info For IPV4 (ICMP Packet Info)
def icmp4_packet(data):
    icmp_type, icmp_code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, icmp_code, checksum


# Extra TCP Info For IPV4 (TCP Packet Info)
def tcp4_packet(data):
    (src_port, dest_port, sequence, acknowledgement, offset_reserved_flag) = struct.unpack('! H H L L H', data[:14])
    return src_port, dest_port, sequence, acknowledgement, offset_reserved_flag


# Extra UDP Info For IPV4 (UDP Packet Info)
def udp4_packet(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]


###########################################################################
# ========================= PACKET INFO IPV6 ============================ #
###########################################################################
# Get IPv6 Packet Header (Number to string)
def ipv6_header(ipv6_next_header):
    if ipv6_next_header == protocolHeaders.TCP:
        ipv6_next_header = "TCP"
    elif ipv6_next_header == protocolHeaders.UDP:
        ipv6_next_header = "UDP"
    elif ipv6_next_header == protocolHeaders.ROUTING:
        ipv6_next_header = "Routing"
    elif ipv6_next_header == protocolHeaders.ICMP:
        ipv6_next_header = "ICMP"
    elif ipv6_next_header == protocolHeaders.ICMPV6:
        ipv6_next_header = "ICMPv6"
    elif ipv6_next_header == protocolHeaders.FRAGMENT:
        ipv6_next_header = "Fragment"
    elif ipv6_next_header == protocolHeaders.HOPOPT:
        ipv6_next_header = "HOPOPT"
    elif ipv6_next_header == protocolHeaders.DESTINATION:
        ipv6_next_header = "Destination"
    elif ipv6_next_header == protocolHeaders.AUTHENTICATING:
        ipv6_next_header = "Authenticating"
    elif ipv6_next_header == protocolHeaders.ENCAPSULING:
        ipv6_next_header = "Encapsuling"
    return ipv6_next_header


# Extra IPv6 Packet Info
def ipv6_packet(data):
    ipv6_first_word, ipv6_payload_legth, ipv6_next_header, ipv6_hoplimit = struct.unpack(
        ">IHBB", data[0:8])
    ipv6_src_ip = socket.inet_ntop(socket.AF_INET6, data[8:24])
    ipv6_dst_ip = socket.inet_ntop(socket.AF_INET6, data[24:40])

    bin(ipv6_first_word)
    "{0:b}".format(ipv6_first_word)
    version = ipv6_first_word >> 28
    traffic_class = ipv6_first_word >> 16
    traffic_class = int(traffic_class) & 4095
    flow_label = int(ipv6_first_word) & 65535

    ipv6_next_header = ipv6_header(ipv6_next_header)
    data = data[40:]

    return data, ipv6_next_header, ipv6_src_ip, ipv6_dst_ip, traffic_class, flow_label


# # Extra ICMP Info For IPV6 (ICMP Packet Info)
def icmp6_packet(data):
    icmpv6_type, icmpv6_code, icmpv6_checksum = struct.unpack(">BBH", data[:4])
    return icmpv6_type, icmpv6_code, icmpv6_checksum


# # Extra TCP Info For IPV6 (TCP Packet Info)
def tcp6_packet(data):
    packet = struct.unpack("!2H2I4H", data[0:20])
    srcPort = packet[0]
    dstPort = packet[1]
    sqncNum = packet[2]
    acknNum = packet[3]
    dataOffset = packet[4] >> 12
    reserved = (packet[4] >> 6) & 0x003F
    tcpFlags = packet[4] & 0x003F
    urgFlag = tcpFlags & 0x0020
    ackFlag = tcpFlags & 0x0010
    pushFlag = tcpFlags & 0x0008
    resetFlag = tcpFlags & 0x0004
    synFlag = tcpFlags & 0x0002
    finFlag = tcpFlags & 0x0001
    window = packet[5]
    checkSum = packet[6]
    urgPntr = packet[7]

    packet = packet[20:]
    return packet, srcPort, dstPort, sqncNum, acknNum, dataOffset, reserved, tcpFlags, urgFlag, ackFlag, pushFlag, resetFlag, synFlag, finFlag, window, checkSum, urgPntr


# # Extra UDP Info For IPV6 (UDP Packet Info)
def udp6_packet(data):
    packet = struct.unpack("!4H", data[0:8])
    srcPort = packet[0]
    dstPort = packet[1]
    lenght = packet[2]
    checkSum = packet[3]

    packet = packet[8:]
    return packet, srcPort, dstPort, lenght, checkSum


###########################################################################
# =============================== Sniffer =============================== #
###########################################################################
def sniffer(wanted_proto, wanted_ver):
    def print_ipv4(version, header_length, ttl, proto, src, target, data):
        dest_mac_formatted = mac_format(dest_mac)
        src_mac_formatted = mac_format(src_mac)
        src_ip_formatted = ip_format(eth_proto, src)
        dest_ip_formatted = ip_format(eth_proto, target)

        if wanted_proto == "ICMP":
            if proto == protocolHeaders.ICMP:
                (icmp_type, icmp_code, checksum) = icmp4_packet(data)

                print("\n" + color.BOLD + "Protocol Header: " + color.END + str(proto))
                print(color.BOLD + "Destination: " + color.END + dest_mac_formatted + " - " + str(dest_ip_formatted))
                print(color.BOLD + "Source: " + color.END + src_mac_formatted + " - " + str(src_ip_formatted))
                print(color.BOLD + "IP Version: " + color.END + str(eth_proto))

                if advanced:
                    print(color.BOLD + "ICMP Packet Info" + color.END)
                    print(color.BOLD + "     ICMP Type: " + color.END + str(icmp_type))
                    print(color.BOLD + "     ICMP Code: " + color.END + str(icmp_code))
                    print(color.BOLD + "     ICMP Checksum: " + color.END + str(checksum))
                    print(color.BOLD + "     ICMP TTL: " + color.END + str(ttl))
                    print(color.BOLD + "     ICMP Header Length: " + color.END + str(header_length))

        elif wanted_proto == "TCP":
            if proto == protocolHeaders.TCP:
                (src_port, dest_port, sequence, acknowledgement, offset_reserved_flag) = tcp4_packet(data)

                print("\n" + color.BOLD + "Protocol Header: " + color.END + str(proto))
                print(color.BOLD + "Destination: " + color.END + dest_mac_formatted + " - " + str(dest_ip_formatted)
                      + " - Port: " + str(dest_port))
                print(color.BOLD + "Source: " + color.END + src_mac_formatted + " - " + str(src_ip_formatted)
                      + " - Port: " + str(src_port))
                print(color.BOLD + "IP Version: " + color.END + str(eth_proto))

                if advanced:
                    print(color.BOLD + "TCP Packet Info" + color.END)
                    print(color.BOLD + "     Sequence Number: " + color.END + str(sequence))
                    print(color.BOLD + "     Acknowledgement: " + color.END + str(acknowledgement))
                    print(color.BOLD + "     Offset Reserved Flag: " + color.END + str(offset_reserved_flag))
                    print(color.BOLD + "     TCP TTL: " + color.END + str(ttl))
                    print(color.BOLD + "     TCP Header Length: " + color.END + str(header_length))

        elif wanted_proto == "UDP":
            if proto == protocolHeaders.UDP:
                (src_port, dest_port, size, data) = udp4_packet(data)

                print(color.BOLD + "Protocol Header: " + color.END + str(proto))
                print(color.BOLD + "Destination: " + color.END + dest_mac_formatted + " - " + str(dest_ip_formatted)
                      + " - Port: " + str(dest_port))
                print(color.BOLD + "Source: " + color.END + src_mac_formatted + " - " + str(src_ip_formatted)
                      + " - Port: " + str(dest_port))
                print(color.BOLD + "IP Version: " + color.END + str(eth_proto))

                if advanced:
                    print(color.BOLD + "UDP Packet Info" + color.END + color.END)
                    print(color.BOLD + "     Size: " + color.END + color.END + str(size))
                    print(color.BOLD + "     UDP TTL: " + color.END + str(ttl))
                    print(color.BOLD + "     UDP Header Length: " + color.END + str(header_length))

    def print_ipv6(newPacket, nextProto, ipv6_src_ip, ipv6_dst_ip, traffic_class, flow_label):
        if wanted_proto == "ICMP":
            if nextProto == "ICMPv6":
                (icmpv6_type, icmpv6_code, icmpv6_checksum) = icmp6_packet(newPacket)

                print("\n" + color.BOLD + "Protocol Header: " + color.END + str(protocolHeaders.ICMPV6))
                print(color.BOLD + "Destination: " + color.END + str(ipv6_dst_ip))
                print(color.BOLD + "Source: " + color.END + str(ipv6_src_ip))
                print(color.BOLD + "IP Version: " + color.END + str(eth_proto))
                if advanced:
                    print(color.BOLD + "ICMPv6 Packet Info" + color.END)
                    print(color.BOLD + "     ICMP Type: " + color.END + str(icmpv6_type))
                    print(color.BOLD + "     ICMP Code: " + color.END + str(icmpv6_code))
                    print(color.BOLD + "     ICMP Checksum: " + color.END + str(icmpv6_checksum))
                    print(color.BOLD + "     ICMP Traffic Class: " + color.END + str(traffic_class))
                    print(color.BOLD + "     ICMP Flow Label: " + color.END + str(flow_label))

        elif wanted_proto == "TCP":
            if nextProto == "TCP":
                (packet, srcPort, dstPort, sqncNum, acknNum, dataOffset, reserved, tcpFlags, urgFlag, ackFlag, pushFlag,
                 resetFlag, synFlag, finFlag, window, checkSum, urgPntr) = tcp6_packet(newPacket)

                print("\n" + color.BOLD + "Protocol Header: " + color.END + str(protocolHeaders.TCP))
                print(color.BOLD + "Destination: " + color.END + str(ipv6_dst_ip) + " - Port: " + str(dstPort))
                print(color.BOLD + "Source: " + color.END + str(ipv6_src_ip) + " - Port: " + str(srcPort))
                print(color.BOLD + "IP Version: " + color.END + str(eth_proto))
                if advanced:
                    print(color.BOLD + "TCPv6 Packet Info" + color.END)
                    print(color.BOLD + "     TCP Sequence Number: " + color.END + str(sqncNum))
                    print(color.BOLD + "     TCP Acknowledge Num: " + color.END + str(acknNum))
                    print(color.BOLD + "     TCP Data Offset: " + color.END + str(dataOffset))
                    print(color.BOLD + "     TCP Reserverd: " + color.END + str(reserved))
                    print(color.BOLD + "     TCP Window: " + color.END + str(window))
                    print(color.BOLD + "     TCP Checksum: " + color.END + str(checkSum))
                    print(color.BOLD + "     TCP Urgent Pointer: " + color.END + str(urgPntr))
                    print(color.BOLD + "     TCP Urgent Pointer: " + color.END + str(urgPntr))
                    if urgFlag == tcpv6Flag.URGENT:
                        print("\tUrgent Flag: Set")
                    if ackFlag == tcpv6Flag.ACKNOWLEDGE:
                        print("\tAck Flag: Set")
                    if pushFlag == tcpv6Flag.PUSHFLAG:
                        print("\tPush Flag: Set")
                    if resetFlag == tcpv6Flag.RESETFLAG:
                        print("\tReset Flag: Set")
                    if synFlag == tcpv6Flag.SYNFLAG:
                        print("\tSyn Flag: Set")
                    if finFlag:
                        print("\tFin Flag: Set")

        elif wanted_proto == "UDP":
            if nextProto == "UDP":
                (packet, srcPort, dstPort, lenght, checkSum) = udp6_packet(newPacket)

                print("\n" + color.BOLD + "Protocol Header: " + color.END + str(protocolHeaders.ICMPV6))
                print(color.BOLD + "Destination: " + color.END + str(ipv6_dst_ip) + " - Port: " + str(dstPort))
                print(color.BOLD + "Source: " + color.END + str(ipv6_src_ip) + " - Port: " + str(srcPort))
                print(color.BOLD + "IP Version: " + color.END + str(eth_proto))
                if advanced:
                    print(color.BOLD + "UDPv6 Packet Info" + color.END)
                    print(color.BOLD + "     UDP Lenght: " + color.END + str(lenght))
                    print(color.BOLD + "     ICMP Checksum: " + color.END + str(checkSum))

    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    try:
        while True:
            raw_data, addr = s.recvfrom(65536)
            dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
            if eth_proto == "IPV4" and wanted_ver == "IPV4":
                (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
                print_ipv4(version, header_length, ttl, proto, src, target, data)
            elif eth_proto == "IPV6" and wanted_ver == "IPV6":
                newPacket, nextProto, ipv6_src_ip, ipv6_dst_ip, traffic_class, flow_label = ipv6_packet(data)
                print_ipv6(newPacket, nextProto, ipv6_src_ip, ipv6_dst_ip, traffic_class, flow_label)
    except KeyboardInterrupt:
        cli_menu()


start()
