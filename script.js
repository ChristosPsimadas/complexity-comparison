
document.getElementById("submitButton").addEventListener("click", async function(event)
{
    event.preventDefault();

    const classA = document.getElementById("classA").value.trim();
    const classB = document.getElementById("classB").value.trim();


    try
    {
        //Send get request
        const response = await fetch(`http://127.0.0.1:5000/api/relationship?classA=${encodeURIComponent(classA)}&classB=${encodeURIComponent(classB)}`);

        if (response.ok)
        {
            //Parse JSON
            const data = await response.json();

            if (data.relationship == "a subset")
            {
                document.getElementById("result").textContent = `${classA} is ${data.relationship} of ${classB}.`;
            }
            else
            {
                document.getElementById("result").textContent = `The relationship between ${classA} and ${classB} is unknown.`;
            }

            console.log(data.relationship);
        }

        else
        {
            document.getElementById("result").textContent = error;

            console.log(error);
        }
    }

    catch (error)
    {
        //Network error
        console.log("Error fetching relationship:", error);
        document.getElementById("result").textContent = "Error: could not fetch the relationship"
    }

});

