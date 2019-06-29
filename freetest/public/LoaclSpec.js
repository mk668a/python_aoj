"use strict";

const Nightmare = require( "nightmare" );
const expect = require( "chai" ).expect;
// const util = require('util');

describe("index.html", function() {
  this.timeout("9s");

  let app;
  let nightmare;
  const BASE_URL = "http://localhost:3035";

  before("start app.js", () => {
    app = require("../app.js");
    return app;
  });

  beforeEach( () => {
    nightmare = new Nightmare({
      // // Uncomment below to display test browser on screen
      // openDevTools: {
      //   mode: "detach"
      // },
      // show: true,
      pollInterval: 50
    });
  });

  it("prints no errors to client console", done => {
    let frontendMessages = [];

    nightmare
    .on('console', function (logType, args) {
      let output = `console.${logType}: ${args}`
      frontendMessages.push(output);
    })
    .on('page', function(type, message, stack){
      let output = `page ${type}: ${message}`
      frontendMessages.push(output);
    })
    .goto( BASE_URL )
    .wait("#textWrapper")
    .end()
    .then( results => {
      expect(frontendMessages).to.be.ok;

      const evalOutputs = function(frontendMessages){
        // makes printable any messages obtained from the frontend console.
        let hasErrors;

        switch (true) {
        case frontendMessages.length === 0:
          console.info("Info: Nothing was printed to frontend console.");
          hasErrors = false;
          break;
        case frontendMessages.length >= 1:
          let output = "The below was printed to frontend console: " +
            frontendMessages.reduce( (text, line) => {
              return `\n ${text} \n ${line}`;
            }) + "\n";
          console.info(output);
          if (output.toLowerCase().search("error") === -1) { hasErrors = false; }
          break;
        default:
          console.error(
              "Error: Console output from frontend is not in the expected format.");
          hasErrors = true;
        }
        return hasErrors;
      };

      let hasErrors = evalOutputs(frontendMessages);

      expect(hasErrors).to.be.false;
      done();
    })
    .catch(done);
  });

  it("contains a #progressText", done => {
    nightmare.goto( BASE_URL )
    .wait(250)
    .exists("#progressText")
    .then( exists => {
      expect(exists).to.be.true;
      done();
    })
    .catch(done);
  });

  describe("timer text", () => {
    it("is in the expected font size", done => {
      nightmare.goto( BASE_URL )
      .wait("#progressText")
      .evaluate( () => {
        let style = window.getComputedStyle(document.querySelector("#progressText"), null);
        return style;
      })
      .end()
      .then( style => {
        expect(style.fontSize).to.equal("40px");
        done();
      })
      .catch(done);
    });

    it("is in expected format ('2 minutes', etc)", done => {
      nightmare.goto( BASE_URL )
      .wait("#progressText")
      .evaluate( () => {
        return document.querySelector("#progressText").innerHTML;
      })
      .then( progressText => {
        expect(progressText).to.contain("minute");
        done();
      })
      .catch(done);
    });

    it("is horizontally aligned to center", done => {
      nightmare.goto( BASE_URL )
      .wait("#progressText")
      .evaluate( () => {
        let style = window.getComputedStyle(document.querySelector("#progressText"), null);
        return style;
      })
      .end()
      .then( style => {
        expect(style.textAlign).to.equal("center");
        done();
      })
      .catch(done);
    });

    it("is in the expected web font", done => {
      nightmare.goto( BASE_URL )
      .wait("#progressText")
      .evaluate( () => {
        let style = window.getComputedStyle(document.querySelector("#progressText"), null);
        return style;
      })
      .end()
      .then( style => {
        expect(style.fontFamily.toLowerCase()).to.contain("overpass");
        done();
      })
      .catch(done);
    });


    it("actually counts down", done => {
      nightmare.goto( BASE_URL )
      .wait("#progressText")
      .wait(2000)
      .evaluate( () => {
        return document.querySelector("#progressText").innerHTML;
      })
      .end()
      .then( result => {
        expect(result).to.contain("1 minute");
        expect(result).to.contain("58 seconds");
        done();
      })
      .catch(done);
    });

    it("displays 'Time Expired' when out of time", done => {
      nightmare.goto( BASE_URL )
      .wait("#progressText")
      .evaluate( () => {
        Pitch.startTime = 0;
        Pitch.endTime = 3000;
        Pitch.start();
        return;
      })
      .wait(3500)
      .evaluate( () => {
        return document.querySelector("#progressText").innerHTML;
      })
      .end()
      .then( result => {
        expect(result).to.contain("Time Expired");
        done();
      })
      .catch(done);

    });
  });

  after( done => {
    app.server.close(done);
  });
});
