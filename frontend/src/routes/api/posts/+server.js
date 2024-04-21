export const POST = async ({ request }) => {
  try {
    const { prompt } = await request.json(); // forespørselskroppen inneholder en "prompt"

    // Gjør en POST-forespørsel til det eksterne API-et med prompten
    const apiResponse = await fetch(
      "https://conexusaiengine.azurewebsites.net/openairoutes",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      }
    );

    if (!apiResponse.ok) {
      throw new Error(`API call failed with status ${apiResponse.status}`);
    }

    const data = await apiResponse.json(); // Anta at API-et returnerer et objekt som inneholder "answer"

    // Send svaret tilbake til klienten
    return new Response(JSON.stringify({ answer: data.answer }), {
      status: 200,
    });
  } catch (error) {
    return new Response(JSON.stringify({ message: error.message }), {
      status: 500,
    });
  }
};

// export async function POST({ request }) {
//     // Hent meldingsteksten fra forespørselskroppen
//     const data = await request.json();
//     const newMessage = {
//         id: messages.length + 1,
//         text: data.text,
//     };
//     messages.push(newMessage);
//     // Returner den nye meldingen med statuskode 201 (Created)
//     return json(newMessage, { status: 201 });
// }
