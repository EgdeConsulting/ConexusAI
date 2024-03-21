using System;
using Microsoft.AspNetCore.Mvc;

namespace dotnetapi
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting the application...");


            // var responseController = new ResponseController();
            // responseController.Get();

            Console.WriteLine("Application finished.");
        }
    }

    [Route("api/[controller]")]
    [ApiController]
    public class ResponseController : ControllerBase
    {
        [HttpGet]
        public ActionResult<string> Get()
        {
            return "Hello World";
        }

        [HttpPost("generate_response")]
        public ActionResult<object> GenerateResponse([FromBody] string prompt)
        {
            if (string.IsNullOrEmpty(prompt))
            {
                return BadRequest(new { error = "No prompt provided" });
            }

            int numLetters = prompt.Count(char.IsLetter);
            string responseMessage = $"Number of letters = {numLetters}";

            return new { response = responseMessage };
        }
    }
}
