using System.Collections;

namespace practica1;
public class VaccinationRequest : ICollectionable
{
    public static readonly String[] Fields = { "Id", "PatientName", "PatientPhone", "Vaccine", "Date", "StartTime", "EndTime" };
    public Hashtable errors = new Hashtable();

    private int id;
    private string patient_name;
    private string patient_phone;
    private string vaccine;
    private string date;
    private string start_time;
    private string end_time;
    
    public override string ToString()
    {
        string str = "";
        for (int i = 0; i < Fields.Length; i ++)
        {
            if (i == Fields.Length-1)
            {
                str += $"{GetType().GetProperty(Fields[i]).GetValue(this, null)}";
            }
            else
            {
                str += $"{GetType().GetProperty(Fields[i]).GetValue(this, null)},";
            }
        }
        return str;
    }

    public int Id
    {
        get => id;
        set
        {
            string valid = Validation.InRange(value, 0, Int32.MaxValue-1);
            if (String.IsNullOrEmpty(valid)){
                id = value;
            }
            else {
                errors.Add("Id", value + " " + valid);
            }
        }
    }

    public string PatientName
    {
        get => patient_name;
        set
        {
            string ValidPatientName = Validation.IsName(value);
            string ValidPatientNameLength = Validation.LengthInRange(value, 2, 20); 
            if (String.IsNullOrEmpty(ValidPatientName) && String.IsNullOrEmpty(ValidPatientNameLength))
            {
                patient_name = value;
            }
            else
            {
                errors.Add("Patient name", value + " " + ValidPatientNameLength + " " + ValidPatientName);
            }
        }
    }

    public string PatientPhone
    {
        get => patient_phone;
        set
        {
            string valid = Validation.IsPhone(value);
            if (String.IsNullOrEmpty(valid))
            {
                patient_phone = value;
            }
            else
            {
                errors.Add("Patient phone", value + " " + valid);
            }
        }
    }

    public string Vaccine
    {
        get => vaccine;
        set
        {
            string valid = Validation.IsVaccine(value);
            if (String.IsNullOrEmpty(valid))
            {
                vaccine = value;
            }
            else
            {
                errors.Add("Vaccine", valid);
            }
        }
    }

    public string Date
    {
        get => date;
        set
        {
            string valid = Validation.IsDate(value);
            if (String.IsNullOrEmpty(valid))
            {
                date = value;
            }
            else
            {
                errors.Add("Date",value + " " + valid);
            }
        }
    }

    public string StartTime
    {
        get => start_time;
        set
        {
            string valid = Validation.IsTime(value);
            if (String.IsNullOrEmpty(valid))
            {
                start_time = value;
            }
            else
            {
                errors.Add("Date",value + " " + valid);
            }
        }
    }

    public string EndTime
    {
        get => end_time;
        set
        {
            string validTime = Validation.IsTime(value);
            if (String.IsNullOrEmpty(validTime))
            { 
                end_time = value;
            }
            else
            {
                errors.Add("Date",value + " " + validTime);
            }
        }
    }

    public void create(Hashtable htParams)
    {
        foreach (var field in GetType().GetProperties())
        {
            var param = Convert.ChangeType(htParams[field.Name], field.PropertyType);
            field.SetValue(this, param, null);
        }
    }
    
    public bool IsValid()
    {
        return !Convert.ToBoolean(errors.Count);
    }
    
    public bool Contain(string s)
    {
        bool res = false;
        string str = "";
        foreach (var field in Fields)
        {
            str += $"{GetType().GetProperty(field).GetValue(this, null)}";
            res = res || str.ToLower().Contains(s.ToLower());
        }

        return res;
    }
    
    public Hashtable Errors()
    {
        return errors;
    }
    
    public string[] GetFields()
    {
        return Fields;
    }
}