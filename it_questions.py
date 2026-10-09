IT_EXIT_EXAM = [
    {
        "id": 1,
        "question": "For an Entity set Citizen, an attribute name 'Address' consists of Street-number, City, and Region. Such an attribute in a database is known as:",
        "options": ["Derived Attribute", "Complex Attribute", "Composite Attribute", "Multi-Valued Attribute"],
        "correct_answer": "Composite Attribute",
        "explanation": "A composite attribute can be divided into smaller sub-parts (e.g., Address divided into Street-number, City, and Region)."
    },
    {
        "id": 2,
        "question": "Which of the following video connectors has an analog variety and a digital variety?",
        "options": ["DVI", "VGA", "DisplayPort", "HDMI"],
        "correct_answer": "DVI",
        "explanation": "DVI has different forms: DVI-A (analog), DVI-D (digital), and DVI-I (integrated analog and digital)."
    },
    {
        "id": 3,
        "question": "What is the most common reason for an unexpected reboot of a computer system?",
        "options": ["Overheating", "Memory leak", "RFI", "ESD damage"],
        "correct_answer": "Overheating",
        "explanation": "Overheating triggers built-in thermal protection mechanisms that force a system to reboot or shut down to prevent permanent hardware damage."
    },
    {
        "id": 4,
        "question": "To view the MAC address table on a Cisco switch, which command can be used?",
        "options": ["S1#show cam table", "S1#show mac table", "S1#show mac address-table", "S1#show mac"],
        "correct_answer": "S1#show mac address-table",
        "explanation": "In Cisco IOS, 'show mac address-table' displays all learned dynamic and static MAC addresses paired with switch ports."
    },
    {
        "id": 5,
        "question": "Which of the following is a valid Visual Basic conditional statement?",
        "options": ["2 < n Or 5", "(2 < n) Or (n < 5)", "2 < n Or < 5", "2 < n < 5"],
        "correct_answer": "(2 < n) Or (n < 5)",
        "explanation": "In Visual Basic, logical expressions must explicitly compare left and right relational evaluations on both sides of operators like 'Or'."
    },
    {
        "id": 6,
        "question": "It's possible to have several methods with the same name that each operate on different arguments. This feature is called method:",
        "options": ["activation", "overflow", "overloading", "expression"],
        "correct_answer": "overloading",
        "explanation": "Method overloading allows multiple methods within the same class to share a name as long as their parameter lists differ."
    },
    {
        "id": 7,
        "question": "Which fiber optic standard utilizes a 50 micron core?",
        "options": ["STP", "Multi-mode", "Single-mode", "UTP"],
        "correct_answer": "Multi-mode",
        "explanation": "Multi-mode optical fiber typically uses either 50 or 62.5 micron core diameters to transmit multiple light modes."
    },
    {
        "id": 8,
        "question": "What effect does a host's wrong default gateway configuration have on network communications?",
        "options": [
            "On the local network, the host is unable to exchange messages",
            "The host is able to connect with hosts on its local network, but not with hosts on other networks",
            "No effect is felt on communication",
            "The host is able to communicate with hosts on distant networks, but not with hosts on the local network"
        ],
        "correct_answer": "The host is able to connect with hosts on its local network, but not with hosts on other networks",
        "explanation": "Local communication uses direct ARP/MAC addressing, but remote subnet communication requires a valid Default Gateway router."
    },
    {
        "id": 9,
        "question": "A tuple takes a ________ value when a record does not have a value for a specific attribute in a database.",
        "options": ["Unknown", "Null", "Not Applicable", "Zero"],
        "correct_answer": "Null",
        "explanation": "A Null value represents missing, unknown, or inapplicable data entries in relational database tables."
    },
    {
        "id": 10,
        "question": "Which HTML attribute specifies a blue background for an inline element or container?",
        "options": ["style=\"background-color:blue\"", "background = \"blue\"", "bgcolor = blue", "bgcolor=#00000"],
        "correct_answer": "style=\"background-color:blue\"",
        "explanation": "Modern HTML5 uses inline CSS via the style attribute (e.g., style=\"background-color:blue\") to set background colors."
    },
    {
        "id": 11,
        "question": "Which Linux command is used for creating a new group in the system?",
        "options": ["chgrp", "chown", "addgrp", "groupadd"],
        "correct_answer": "groupadd",
        "explanation": "The 'groupadd' utility creates a new user group definition in Linux user administration."
    },
    {
        "id": 12,
        "question": "Which Java Thread method waits for a thread to complete or terminate before continuing execution?",
        "options": ["isAlive()", "sleep()", "join()", "stop()"],
        "correct_answer": "join()",
        "explanation": "The join() method pauses execution of the current thread until the target thread finishes execution."
    },
    {
        "id": 13,
        "question": "Which routing protocol generally has the least amount of administrative overhead and resources on small networks?",
        "options": ["OSPF", "BGP", "EIGRP", "RIP"],
        "correct_answer": "RIP",
        "explanation": "Routing Information Protocol (RIP) is simple to configure and consumes minimal memory/CPU overhead compared to link-state protocols like OSPF."
    },
    {
        "id": 14,
        "question": "Which Cisco IOS command can you use to view active NAT translations on a router?",
        "options": ["Router#show nat translations", "Router#debug ip nat translations", "Router#show ip nat translations", "Router#show translations nat"],
        "correct_answer": "Router#show ip nat translations",
        "explanation": "'show ip nat translations' displays all active source/destination Network Address Translation mappings."
    },
    {
        "id": 15,
        "question": "Which command can be used on a Windows host to display the local IP routing table?",
        "options": ["show ip route", "tracert", "netstat -s", "netstat -r"],
        "correct_answer": "netstat -r",
        "explanation": "On Windows Command Prompt, 'netstat -r' (or 'route print') displays the system's IP routing table."
    },
    {
        "id": 16,
        "question": "Which SQL constraint enforces referential integrity between related database tables?",
        "options": ["PRIMARY KEY (ID)", "UNIQUE (ID)", "FOREIGN KEY (ID) REFERENCES Table_name(ID)", "ID CHAR(90) NOT NULL"],
        "correct_answer": "FOREIGN KEY (ID) REFERENCES Table_name(ID)",
        "explanation": "Foreign keys enforce referential integrity by ensuring child table keys match valid primary key entries in a parent table."
    },
    {
        "id": 17,
        "question": "When moving from the outside edge of an HTML box element inwards, in what order do margin, border, and padding occur?",
        "options": ["border, padding, margin", "padding, border, margin", "margin, border, padding", "margin, padding, border"],
        "correct_answer": "margin, border, padding",
        "explanation": "The CSS Box Model order from outside to inside is: Margin ➔ Border ➔ Padding ➔ Content."
    },
    {
        "id": 18,
        "question": "In Java exception handling, which class serves as the superclass for all exception and error types?",
        "options": ["String", "Catchable", "Throwable", "RuntimeExceptions"],
        "correct_answer": "Throwable",
        "explanation": "java.lang.Throwable is the root superclass of all Exceptions and Errors in the Java language hierarchy."
    },
    {
        "id": 19,
        "question": "Which optical disc format provides up to 25 GB of storage on a single-sided, single-layer disc?",
        "options": ["Double-sided, single-layer DVD-R", "Double-sided, double-layer DVD+R", "Double-sided, single-layer DVD+R", "Single-sided, single-layer Blu-ray Disc"],
        "correct_answer": "Single-sided, single-layer Blu-ray Disc",
        "explanation": "Standard single-layer Blu-ray Discs hold up to 25 GB of data."
    },
    {
        "id": 20,
        "question": "After renaming VLAN 3 on a Cisco switch, which command validates the configuration changes for that specific VLAN?",
        "options": ["Switch#show interface vlan 3", "Switch#show run", "Switch#show vlan id 3", "Switch#show vlans"],
        "correct_answer": "Switch#show vlan id 3",
        "explanation": "'show vlan id <id>' displays status, name, and port assignment information for a single VLAN number."
    }
]
