import TextBlock from './TextBlock';
import VocabTable from './VocabTable';
import GrammarBox from './GrammarBox';
import ExampleBlock from './ExampleBlock';
import TipBox from './TipBox';
import VideoBlock from './VideoBlock';

const componentMap = {
  text: TextBlock,
  vocab: VocabTable,
  grammar: GrammarBox,
  example: ExampleBlock,
  tip: TipBox,
  video: VideoBlock,
};

export default function SectionRenderer({ section }) {
  const Component = componentMap[section.type];

  if (!Component) {
    return (
      <div className="p-4 bg-error/10 border border-error/30 rounded-xl text-error">
        Άγνωστος τύπος ενότητας: {section.type}
      </div>
    );
  }

  return <Component content={section.content_json} />;
}
