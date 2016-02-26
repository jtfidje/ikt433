package Server;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Client implements Runnable{
	private Socket socket;
	
	private HashMap<String, ArrayList<HashMap<String, String>>> people;
	
	public String user;
	
	public PrintWriter out;
	
	public Client(Socket s){
		socket = s;
		people = new HashMap<String, ArrayList<HashMap<String, String>>>();
		try {
			JSONParser parser = new JSONParser();
			Object obj = parser.parse(new FileReader("people.json"));
			JSONObject jsonObject = (JSONObject) obj;

			Iterator<String> keys = jsonObject.keySet().iterator();

			while(keys.hasNext()) {
			    String key = (String)keys.next();
			    ArrayList arr = (ArrayList)jsonObject.get(key);
			    ArrayList<HashMap<String, String>> arr2 = new ArrayList<HashMap<String, String>>();
			    for (int i = 0; i < arr.size(); i++) {
			    	HashMap<String, String> dict = (HashMap<String, String>)arr.get(i);
			    	arr2.add(dict);
				}
			    people.put(key, arr2);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ParseException e) {
			e.printStackTrace();
		}
	}

	@SuppressWarnings("resource")
	@Override
	public void run(){
		try{
			// The socket input stream
			Scanner in = new Scanner(socket.getInputStream());

			// The socket output stream
			out = new PrintWriter(socket.getOutputStream());
			
			// Ask for username before entering while-loop
			out.println("Enter username:\n");
			out.flush();
			if(in.hasNext()){
				this.user = in.nextLine();
				System.out.println("User: " + this.user);
				out.println("Welcome " + this.user);
				out.flush();
			}
			
			while(true){
				if(in.hasNext()){
					// Get input from input stream
					String input = in.nextLine();
					String[] inputArray = input.split("\\s+");
					System.out.println("Command: " + input);
					String result = "";
					
					switch (inputArray[0]) {
					case "getmail1":
						result = getmail1(inputArray);
						break;
					
					case "getmail2":
						result = getmail2(inputArray);
						break;
					
					case "getphone1":
						result = getphone1(inputArray);
						break;
						
					case "getphone2":
						result = getphone2(inputArray);
						break;
						
					case "getall":
						result = getall();
						break;
						
					case "getonline":
						result = Main.getOnline();
						break;
						
					case "relay":
						relayMsg(inputArray);
						continue;
						
					case "reply":
						Main.sendAck(inputArray[1]);
						continue;
						
					default:
						result = "Unknown command: " + input;
					}
					
					// Resend message to client as ack
					out.println(result + "\n");
					out.flush();
				}
			}
		} catch(Exception e){
			// Print error if any
			e.printStackTrace();
		}
	}

	public String getmail1(String[] cmd){
		String name = cmd[2];
		String dept = cmd[1];
		ArrayList<HashMap<String, String>> deptList = people.get(dept);
		for (HashMap<String, String> hashMap : deptList) {
			if (hashMap.get("lastName").equals(name)){
				return hashMap.get("email");
			}
		}
		return "Couldn't find student/employee";
	}
	
	public String getmail2(String[] cmd){
		String first = cmd[1];
		String last = cmd[2];
		
		for (Map.Entry<String, ArrayList<HashMap<String, String>>> entry : people.entrySet()) {
			ArrayList<HashMap<String, String>> deptList = (ArrayList<HashMap<String, String>>) entry.getValue();
	        for (HashMap<String, String> hashMap : deptList) {
				if (hashMap.get("firstName").equals(first) && hashMap.get("lastName").equals(last)){
					return hashMap.get("email");
				}
			}
	    }
		return "Couldn't find student/employee";
	}
	
	public String getphone1(String[] cmd){
		String name = cmd[2];
		String dept = cmd[1];
		ArrayList<HashMap<String, String>> deptList = people.get(dept);
		for (HashMap<String, String> hashMap : deptList) {
			if (hashMap.get("lastName").equals(name)){
				return hashMap.get("phone");
			}
		}
		return "Couldn't find student/employee";
	}
	
	public String getphone2(String[] cmd){
		String first = cmd[1];
		String last = cmd[2];
		
		for (Map.Entry<String, ArrayList<HashMap<String, String>>> entry : people.entrySet()) {
			ArrayList<HashMap<String, String>> deptList = (ArrayList<HashMap<String, String>>) entry.getValue();
	        for (HashMap<String, String> hashMap : deptList) {
				if (hashMap.get("firstName").equals(first) && hashMap.get("lastName").equals(last)){
					return hashMap.get("phone");
				}
			}
	    }
		return "Couldn't find student/employee";
	}
	
	public String getall(){
		String string = "";
		
		for (Map.Entry<String, ArrayList<HashMap<String, String>>> entry : people.entrySet()) {
			ArrayList<HashMap<String, String>> deptList = (ArrayList<HashMap<String, String>>) entry.getValue();
	        for (HashMap<String, String> hashMap : deptList) {
				string += ("\n\n" + hashMap.get("firstName") + " " + hashMap.get("lastName"));
				string += ("\n" + hashMap.get("email"));
				string += ("\n" + hashMap.get("phone"));
				string += ("\n" + "Department " + entry.getKey());
			}
	    }
		
		return string;
	}
	
	public void relayMsg(String[] cmd){
		String user = cmd[1];
		List<String> msgArr = new ArrayList<String>(Arrays.asList(cmd));
		msgArr.remove(0); // Removes 'relay'
		msgArr.remove(0); // Remove username
	
		String msg = "";
		
		for(String s : msgArr){
			msg += s + " ";
		}
		
		Main.relayMsg(msg, user, this.user);
	}
}