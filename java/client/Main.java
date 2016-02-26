package Client;
import java.io.IOException;
import java.net.Socket;

public class Main{
	private final static int PORT = 60000;
	private final static String HOST = "localhost";

	public static void main(String[] args) throws IOException{
		try{
			// Connect to server on HOST and PORT
			Socket s = new Socket(HOST, PORT);

			System.out.println("You connected to " + HOST);

			// Start a client object
			Client client = new Client(s);
			
			// Start client in new thread
			Thread t = new Thread(client);
			t.start();
		} catch (Exception e){
			e.printStackTrace();
		}
	}	
}