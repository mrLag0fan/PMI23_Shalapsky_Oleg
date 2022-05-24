namespace practica1;

public class MainFile
{
    static void Main(string[] args)
    {

        VRList<VaccinationRequest> collection = new VRList<VaccinationRequest>();
        while (true)
        {
            Console.WriteLine(@"
            1. Read from file
            2. Print
            3. Add new
            4. Delete by Id
            5. Edit by Id
            6. Search
            7. Sort by field
            ");
            int menu;
            try
            {
                menu = Int32.Parse(Console.ReadLine());
            }
            catch (FormatException e)
            {
                Console.WriteLine(e.Message);
                continue;
            }

            switch (menu)
            {
                case 1:
                    Console.WriteLine("Enter file path");
                    string path = Console.ReadLine(); 
                    collection.AddDataFromFile(path);
                    break;
                case 2:
                    collection.PrintAll();
                    break;
                case 3:
                    Console.WriteLine("Input values");
                    string str = "Order: ";
                    foreach (var field in new VaccinationRequest().GetFields())
                    {
                        str += field + ",";
                    }
                    Console.WriteLine(str);
                    collection.AddFromLine(Console.ReadLine());
                    break;
                case 4:
                    Console.WriteLine("Input Id:");
                    string id = Console.ReadLine();
                    if (!collection.Delete(id))
                    {
                        Console.WriteLine("Wrong");
                    }
                    break;
                case 5:
                    Console.WriteLine("Input Id:");
                    string val = Console.ReadLine();
                    if (!collection.Edit(val))
                        Console.WriteLine("Wrong");
                    break;
                case 6:
                    Console.WriteLine("Input search param:");
                    string param = Console.ReadLine();
                    collection.Search(param).PrintAll();
                    break;
                case 7:
                    Console.WriteLine("Input sort param one of:");
                    foreach (var field in VaccinationRequest.Fields)
                    {
                        Console.Write(field + " ");
                    }
                    
                    string sortParam = Console.ReadLine();
                    collection.SortBy(sortParam);
                    collection.PrintAll();
                    break;
            }
        }
    }
}