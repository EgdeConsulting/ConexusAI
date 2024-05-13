export const GET = async ({ request }) => {
  const autherHeader = request.headers.get("Authorization");

  // if (autherHeader !== 'ConexusAI') {
  //     return new Response(JSON.stringify({message:'Unauthorized: invalid credentials'}), { status: 401 });
  // }
  const res = await fetch("https://python-chat-api.onrender.com/python/prompt");
  const data = await res.json();

  return new Response(JSON.stringify({ data }), { status: 200 });
};
export const POST = async ({ request }) => {
  try {
    const { prompt } = await request.json(); // forespørselskroppen inneholder en "prompt"

    // Gjør en POST-forespørsel til det eksterne API-et med prompten
    const apiResponse = await fetch(
      "https://restapipython.azurewebsites.net/query",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      }
    );

    if (!apiResponse.ok) {
      throw new Error(`API call failed with status ${apiResponse.status}`);
    }

    const data = await apiResponse.json(); // API-svaret inneholder et "answer"

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
