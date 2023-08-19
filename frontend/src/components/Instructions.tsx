const Instructions: React.FC = () => {
  return (
    <div className="flex flex-col border-2 border-gray-800 mt-[37px] p-4 rounded-[24px]">
      <h3 className="text-gray-200">
        How To Create a Test Case With This Generator
      </h3>
      <ol className="text-gray-400 space-y-[2px] mt-[16px]">
        <li>1. Insert User story context as a one paragraph in to the first text field</li>
        <li>2. Click “Generate” to create the test cases according to the acceptance criteria.</li>
        <li>3. Use save to Excel functionality to export the test cases</li>
      </ol>
    </div>
  );
};

export default Instructions;