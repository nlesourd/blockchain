    #from https://github.com/TomSchimansky/CustomTkinter#

import customtkinter
import tkinter
import blockchain as bc


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Block chain and cryptographic security")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #creation of initial nodes
        self.current_node = None

        self.node0 = bc.Node(authority=True)
        self.node1 = bc.Node()
        self.node2 = bc.Node()
        self.node3 = bc.Node()

        self.transaction0 = bc.Transaction(self.node0.public_key, self.node1.public_key, 12345)
        self.node0.transaction_signing(self.transaction0)
        self.node1.transaction_verification(self.transaction0)        
        self.node0.transaction_validation(self.transaction0)

        self.transaction1 = bc.Transaction(self.node0.public_key, self.node1.public_key, 23456)
        self.node0.transaction_signing(self.transaction1)    

        self.block0 = bc.Block(self.node0.public_key, self.transaction0.data)
        self.node0.block_signing(self.block0)
        self.node1.block_verification(self.block0)
        self.node0.block_validation(self.block0)

        self.block0 = bc.Block(self.node0.public_key, self.transaction1.data)
        self.node0.block_signing(self.block0)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.node_selection_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Node selection",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.node_selection_button_event)
        self.node_selection_button.grid(row=1, column=0, sticky="ew")

        self.verified_transactions_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Verified transactions",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.verified_transactions_button_event)
        self.verified_transactions_button.grid(row=2, column=0, sticky="ew")

        self.pending_transactions_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Pending transactions",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.pending_transactions_button_event)
        self.pending_transactions_button.grid(row=3, column=0, sticky="ew")

        self.verified_blocks_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Verified blocks",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.verified_blocks_button_event)
        self.verified_blocks_button.grid(row=4, column=0, sticky="ew")

        self.pending_blocks_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Pending blocks",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.pending_blocks_button_event)
        self.pending_blocks_button.grid(row=5, column=0, sticky="ew")


        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create node selection frame
        self.node_selection_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.node_selection_frame.grid(row=0, column=1, sticky="nsew")
        self.node_selection_frame.grid_rowconfigure(0, weight=1)
        self.node_selection_frame.grid_columnconfigure(1, weight=1)

        #create node navigation
        self.navigation_node_frame = customtkinter.CTkFrame(self.node_selection_frame, corner_radius=0)
        self.navigation_node_frame.grid_rowconfigure(7, weight=1)

        #create node navigation buttons
        self.create_transaction_button = customtkinter.CTkButton(self.navigation_node_frame, corner_radius=0, height=40, border_spacing=10, text="Create transaction",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.create_transaction_button_event)
        self.create_transaction_button.grid(row=1, column=0, sticky="ew")

        self.verify_transaction_button = customtkinter.CTkButton(self.navigation_node_frame, corner_radius=0, height=40, border_spacing=10, text="Verify transaction",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.verify_transaction_button_event)
        self.verify_transaction_button.grid(row=2, column=0, sticky="ew")

        self.create_block_button = customtkinter.CTkButton(self.navigation_node_frame, corner_radius=0, height=40, border_spacing=10, text="Create block",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.create_block_button_event)
        self.create_block_button.grid(row=3, column=0, sticky="ew")

        self.verify_block_button = customtkinter.CTkButton(self.navigation_node_frame, corner_radius=0, height=40, border_spacing=10, text="Verify block",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.verify_block_button_event)
        self.verify_block_button.grid(row=4, column=0, sticky="ew")

        self.transactions_created_button = customtkinter.CTkButton(self.navigation_node_frame, corner_radius=0, height=40, border_spacing=10, text="Transactions created",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.transactions_created_button_event)
        self.transactions_created_button.grid(row=5, column=0, sticky="ew")

        self.transactions_pending_button = customtkinter.CTkButton(self.navigation_node_frame, corner_radius=0, height=40, border_spacing=10, text="Transactions pending",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.transactions_pending_button_event)
        self.transactions_pending_button.grid(row=6, column=0, sticky="ew")

        #create selection node
        self.node_info_frame = customtkinter.CTkFrame(self.node_selection_frame, corner_radius=0, fg_color="transparent")
        self.node_info_frame.grid_rowconfigure(4, weight=1)
        self.node_info_frame.grid(row=0, column=1, sticky="nsew")

        nodes_id = ["Node " + str(node.id) for node in self.node0.network]
        self.node_menu = customtkinter.CTkOptionMenu(self.node_info_frame,
                                            values=nodes_id,
                                            command=self.node_selection_optionmenu_event)
        self.node_menu.grid(row=0, column=0, padx=20, pady=20)

        #create transaction frame
        self.create_transaction_frame  = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")

        self.recipient_label = customtkinter.CTkLabel(self.create_transaction_frame,text="Recipient id")
        self.recipient_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.recipient_entry = customtkinter.CTkEntry(self.create_transaction_frame, placeholder_text="0, 1...")
        self.recipient_entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
 
        self.data_label = customtkinter.CTkLabel(self.create_transaction_frame, text="Data")
        self.data_label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.data_entry = customtkinter.CTkEntry(self.create_transaction_frame, placeholder_text="12345")
        self.data_entry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.create_transaction_submit = customtkinter.CTkButton(self.create_transaction_frame, text="Submit", command=self.create_transaction_submit_event)
        self.create_transaction_submit.grid(row=2, column=1)


        #verify transaction frame
        self.verify_transaction_frame  = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")

        self.transaction_label = customtkinter.CTkLabel(self.verify_transaction_frame,text="Transaction id")
        self.transaction_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.transaction_entry = customtkinter.CTkEntry(self.verify_transaction_frame, placeholder_text="0, 1...")
        self.transaction_entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.verify_transaction_submit = customtkinter.CTkButton(self.verify_transaction_frame, text="Submit", command=self.verify_transaction_submit_event)
        self.verify_transaction_submit.grid(row=2, column=1)

        #create block frame
        self.create_block_frame  = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")

        self.transaction_b_label = customtkinter.CTkLabel(self.create_block_frame,text="Transaction id")
        self.transaction_b_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.transaction_b_entry = customtkinter.CTkEntry(self.create_block_frame, placeholder_text="0, 1...")
        self.transaction_b_entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.block_creation_submit = customtkinter.CTkButton(self.create_block_frame, text="Submit", command=self.block_creation_submit_event)
        self.block_creation_submit.grid(row=2, column=1)

        #verify block frame
        self.verify_block_frame  = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")

        self.block_label = customtkinter.CTkLabel(self.verify_block_frame,text="Block id")
        self.block_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.block_entry = customtkinter.CTkEntry(self.verify_block_frame, placeholder_text="0, 1...")
        self.block_entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.block_verify_submit = customtkinter.CTkButton(self.verify_block_frame, text="Submit", command=self.block_verify_submit_event)
        self.block_verify_submit.grid(row=2, column=1)

        #transactions created
        self.transactions_created_frame  = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")

        #transactions pending
        self.transactions_pending_frame  = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")

        #create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #create third frame 
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #create fifth frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("node_selection")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.node_selection_button.configure(fg_color=("gray75", "gray25") if name == "node_selection" else "transparent")
        self.verified_transactions_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.pending_transactions_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.verified_blocks_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.pending_blocks_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # show selected frame
        if name == "node_selection":
            self.node_selection_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.node_selection_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()

    def select_frame_action_by_name(self, name):
        self.create_transaction_button.configure(fg_color=("gray75", "gray25") if name == "create_transaction" else "transparent")
        self.verify_transaction_button.configure(fg_color=("gray75", "gray25") if name == "verify_transaction" else "transparent")
        self.create_block_button.configure(fg_color=("gray75", "gray25") if name == "create_block" else "transparent")
        self.verify_block_button.configure(fg_color=("gray75", "gray25") if name == "verify_block" else "transparent")
        self.transactions_created_button.configure(fg_color=("gray75", "gray25") if name == "transactions_verified" else "transparent")
        self.transactions_pending_button.configure(fg_color=("gray75", "gray25") if name == "transactions_pending" else "transparent")

        if name == "create_transaction":
            self.create_transaction_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.create_transaction_frame.grid_forget()
        
        if name == "verify_transaction":
            self.verify_transaction_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.verify_transaction_frame.grid_forget()

        if name == "create_block":
            self.create_block_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.create_block_frame.grid_forget()

        if name == "verify_block":
            self.verify_block_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.verify_block_frame.grid_forget()

        if name == "transactions_created":
            self.transactions_created_frame = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")
            tc = "Transaction(s) created by Node " + str(self.current_node.id) + ":"
            if len(self.current_node.get_transactions_created(self.transaction0)) > 0:
                tc += "\n \n"
                for id in self.current_node.get_transactions_created(self.transaction0):
                    tc += "Transaction " + str(id) + "\n"

            transactions_created_label = customtkinter.CTkLabel(self.transactions_created_frame,text=tc)
            transactions_created_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
            self.transactions_created_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.transactions_created_frame.grid_forget()

        if name == "transactions_pending":
            self.transactions_pending_frame = customtkinter.CTkFrame(self.node_info_frame, corner_radius=0, fg_color="transparent")
            tc = "Transaction(s) pending for Node " + str(self.current_node.id) + ":"
            if len(self.current_node.get_transactions_pending(self.transaction0)) > 0:
                tc += "\n \n"
                for id in self.current_node.get_transactions_pending(self.transaction0):
                    transaction = self.transaction0.transactions[id]
                    tc += "Transaction " + str(id) + "\n"
                    tc += "Hash: " + str(transaction.hash) + "\n"
                    tc += "Digital signature decrypted: " + str(transaction.digital_signature_decrypted()) + "\n \n"

            transactions_pending_label = customtkinter.CTkLabel(self.transactions_pending_frame,text=tc)
            transactions_pending_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
            self.transactions_pending_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.transactions_pending_frame.grid_forget()

    def node_selection_button_event(self):
        self.select_frame_by_name("node_selection")

    def verified_transactions_button_event(self):
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        verified_transactions = "List of verified transactions:"
        if len(self.transaction1.get_verified_transactions()) > 0:
            verified_transactions += "\n \n" + "".join(["Transaction " + str(id_transaction) + " \n" for id_transaction in self.transaction1.get_verified_transactions()])

        self.label_verified_transactions = customtkinter.CTkLabel(self.second_frame, text=verified_transactions)
        self.label_verified_transactions.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.select_frame_by_name("frame_2")

    def pending_transactions_button_event(self):
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        pending_transactions = "List of pending transactions:\n\n"
        
        if len(self.transaction0.get_pending_transactions()) > 0:
            for id_transaction in self.transaction0.get_pending_transactions():
                transaction = self.transaction0.transactions[id_transaction]
                pending_transactions += "Transaction " + str(id_transaction) + ":\n"
                pending_transactions += "node(s) who verified: " + transaction.who_verified() + "\n"
                pending_transactions += "node(s) who not verified: " + transaction.who_not_verified(self.node0) + "\n"
                pending_transactions += "hash: " + str(transaction.hash) + "\n"
                pending_transactions += "digital signature decrypted: " + str(transaction.digital_signature_decrypted()) + "\n\n"
        
        self.label_pending_transactions = customtkinter.CTkLabel(self.third_frame, text=pending_transactions)
        self.label_pending_transactions.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        self.select_frame_by_name("frame_3")

    def verified_blocks_button_event(self):
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        verified_blocks = "List of verified blocks:"
        if len(self.block0.get_verified_blocks()) > 0:
            verified_blocks += "\n\n" + "".join(["Block " + str(id_block) + " \n" for id_block in self.block0.get_verified_blocks()])
        
        self.label_verified_blocks = customtkinter.CTkLabel(self.fourth_frame, text=verified_blocks)
        self.label_verified_blocks.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.select_frame_by_name("frame_4")

    def pending_blocks_button_event(self):
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        pending_blocks = "List of pending blocks: \n\n"

        if len(self.block0.get_pending_blocks()) > 0:
            for id_block in self.block0.get_pending_blocks():
                block = self.block0.chain[id_block]
                pending_blocks += "Block " + str(id_block) + ":\n"
                pending_blocks += "node(s) who verified: " + block.who_verified_blocks() + "\n"
                pending_blocks += "node(s) who not verified: " + block.who_not_verified_blocks(self.node0) + "\n"
                pending_blocks += "hash: " + str(block.hash) + "\n"
                pending_blocks += "digital signature decrypted: " + str(block.digital_signature_decrypted()) + "\n\n"

            
        self.label_pending_blocks = customtkinter.CTkLabel(self.fifth_frame, text=pending_blocks)
        self.label_pending_blocks.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.select_frame_by_name("frame_5")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def node_selection_optionmenu_event(self, node_id):
        self.current_node = self.node0.network[int(node_id[-1])]
        self.navigation_node_frame.grid(row=0, column=0, sticky="nsew")

        info_node = "Id: "+ str(self.current_node.id) + ", Authority: "+ str(self.current_node.authority) + ", Public key: e = "+ str(self.current_node.public_key[0]) + "\n"
        info_node += "Public key: n = "+ str(self.current_node.public_key[1])[:10] + " (first 10 digits) \n"
        label_node_info = customtkinter.CTkLabel(self.node_info_frame, text=info_node)
        label_node_info.grid(row=1, column=0, padx=20, pady=0)

    def create_transaction_button_event(self):
        self.select_frame_action_by_name("create_transaction")

    def verify_transaction_button_event(self):
        self.select_frame_action_by_name("verify_transaction")
    
    def create_block_button_event(self):
        self.select_frame_action_by_name("create_block")

    def verify_block_button_event(self):
        self.select_frame_action_by_name("verify_block")

    def transactions_created_button_event(self):
        self.select_frame_action_by_name("transactions_created")

    def transactions_pending_button_event(self):
        self.select_frame_action_by_name("transactions_pending")

    def create_transaction_submit_event(self):
        recipient_id = self.recipient_entry.get()
        sender = self.current_node
        recipient = self.node0.network[int(recipient_id)]
        data = self.data_entry.get()
        sender.create_transaction(recipient.public_key, data)
    
    def verify_transaction_submit_event(self):
        id_transaction = self.transaction_entry.get()
        transaction = self.transaction0.transactions[int(id_transaction)]
        self.current_node.transaction_verification(transaction)

    def block_creation_submit_event(self):
        id_transaction = self.transaction_b_entry.get()
        transaction = self.transaction0.transactions[int(id_transaction)]
        self.current_node.add_transaction_to_blockchain(transaction)

    def block_verify_submit_event(self):
        id_block = self.block_entry.get()
        block = self.block0.chain[int(id_block)]
        self.current_node.block_verification(block)


if __name__ == "__main__":
    app = App()
    app.mainloop()
