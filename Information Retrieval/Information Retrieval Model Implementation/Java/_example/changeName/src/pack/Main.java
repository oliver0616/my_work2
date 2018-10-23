package pack;

import java.io.File;

public class Main {
	public static void main(String[] args) {
		
		File folder = new File("//Users//chenh15//eclipse-workspace//changeName//files");
		//File result = new File("//Users//chenh15//eclipse-workspace//changeName//files");
   	 	File[] listOfFiles = folder.listFiles();
   	 	for (File file : listOfFiles) {
   	 		//System.out.println(file);
   	 		String newName = file.getName()+".txt";
   	 		File result = new File("//Users//chenh15//eclipse-workspace//changeName//files//"+newName);
   	 		boolean success = file.renameTo(result);
   		}
   	 	
	}
}
