package Client;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Client implements Runnable {
	private Socket socket;
	private Thread listenThread;
	private Thread sendThread;

	PrintWriter out;
	
	public Client(Socket s){
		socket = s;
	}

	@SuppressWarnings("resource")
	@Override
	public void run(){
		sendThread = new Thread(new Runnable() {
	         public void run(){
	        	try{
	        		// Get socket output stream
	    			out = new PrintWriter(socket.getOutputStream());
	        		
	        		// Gets input stream from command line
		 			Scanner chat = new Scanner(System.in);
		 			
		 			// Get username before entering while-loop
		 			String user = chat.nextLine();
					out.println(user);
					out.flush();
		 			
		        	while(true){
			        	// Gets input from command line stream
						String input = chat.nextLine();
						
						// Send input from command line to server
						out.println(input);
						out.flush();
		        	}
	        	} catch(Exception e){
	        		e.printStackTrace();
	        	}
	         }
		});
		
		listenThread = new Thread(new Runnable() {
	         public void run(){
	              try{
	            	// Gets socket input stream
			 		Scanner in = new Scanner(socket.getInputStream());
			 		
			 		while(true) {
						String input = in.nextLine();
						String[] inputArray = input.split("\\s+");
						if(inputArray[0].equals("relay")){
							Client.this.out.println("reply " + inputArray[1] + " ACK!");
							Client.this.out.flush();
							
							List<String> arr = new ArrayList<String>(Arrays.asList(inputArray));
							arr.remove(0); // Remove 'relay'
							arr.remove(0); // Remove username
							
							input = "";
							
							for(String s : arr){
								input += s + " ";
							}
						}
						
						System.out.println(input);
					}
	              }catch(Exception e){
	            	  e.printStackTrace();
	              }
	         }
		});
		
		listenThread.start();
		sendThread.start();
	}
}