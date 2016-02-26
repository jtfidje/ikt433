package Server;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.ServerSocket;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.ArrayList;

public class Main{
	public static HashMap<String, ArrayList<HashMap<String, String>>> people;
	private static ArrayList<Thread>threads;
	private static ArrayList<Client>clients;
	
	@SuppressWarnings({ "unchecked", "resource" })
	public static void main(String[] args) throws IOException {
		try{
			// Init. list to hold threads
			threads = new ArrayList<Thread>();
			clients = new ArrayList<Client>();

			// Port to use when accepting connections
			final int PORT = 60000;

			// Create server on PORT
			ServerSocket server = new ServerSocket(PORT);
			
			System.out.println("Waiting for clients...");

			while(true){
				// Accept connections
				Socket s = server.accept();

				System.out.println("Client connected from " + s.getLocalAddress().getHostName());
				
				// Create client object
				Client chat = new Client(s);
				
				// Start new thread with connected client
				Thread t = new Thread(chat);
				t.start();
				
				// Add client and thread to list
				clients.add(chat);
				threads.add(t);
			}
		} catch(Exception e){
			System.out.println("An error occured.");
			e.printStackTrace();
		}
	}
	
	public static String getOnline(){
		String users = "";
		for(Client client : clients){
			users += "\n" + client.user;
		}
		
		return users;
	}
	
	public static void relayMsg(String msg, String toUser, String fromUser){
		for(Client client : clients){
			if(client.user.equals(toUser)){
				client.out.println("relay " + fromUser + " " + msg);
				client.out.flush();
			}
		}
	}
	
	public static void sendAck(String user){
		for(Client client : clients){
			if(client.user.equals(user)){
				client.out.println("ACK!");
				client.out.flush();
			}
		}
	}
}