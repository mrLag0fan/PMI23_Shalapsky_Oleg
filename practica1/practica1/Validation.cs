using System.Globalization;
using System.Text.RegularExpressions;

namespace practica1;

public class Validation
{
    
    private static readonly Regex NameRegex = new Regex(@"\A(?!['-])(?!.*['-]{2})[A-Za-z'-]+(?<!['-])\z");
    private static readonly Regex PhoneRegex = new Regex(@"\++((380+\d{9})|(7+\d{10})|(48+\d{9}))");
    private static readonly List<string> VaccineTypes = new List<string>(new []{"pfizer", "moderna", "AstraZeneca"});
    
    public static string InRange(dynamic value, dynamic min, dynamic max)
    {
        if (value >= min && value <= max)
        {
            return "";
        }
        else
        {
            return value + " must be in range[" + min + "," + max + "]";
        }
    }

    public static string IsName(string value)
    {
        if (NameRegex.IsMatch(value))
        {
            return "";
        }

        return "Is not a patient name";
    }
    
    public static string LengthInRange(string value, int min, int max)
    { 
        int valueLength = value.Length;
        if (valueLength > min && valueLength < max)
        {
            return "";
        }

        return "Value length " + value.Length + " must be in range(" + min + "," + max + ")";
    }

    public static string IsPhone(string value)
    {
        if (PhoneRegex.IsMatch(value))
        {
            return "";
        }

        return "Is mot a phone";
    }

    public static string IsVaccine(string value)
    {
        foreach (var v in VaccineTypes)
        {
            if (value.ToUpper().Equals(v.ToUpper()))
            {
                return "";
            }
        }
        return value + " must be one of " + String.Join(", ", VaccineTypes.ToArray());
    }
    
    public static string IsDate(string value)
    {
        try
        {
            DateTime date = DateTime.Parse(value);
            return "";
        }
        catch (Exception e)
        {
            return "Is not date";
        }
    }
    
    public static string IsTime(string value)
    {
        try
        {
            DateTime date = DateTime.ParseExact(value, "HH:mm", CultureInfo.InvariantCulture);
            return "";
        }
        catch (Exception e)
        {
            return "Is not time";
        }
    }
}