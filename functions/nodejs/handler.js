exports.hello = async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Hello from Node.js Function!',
      input: event,
    }),
  };
};
