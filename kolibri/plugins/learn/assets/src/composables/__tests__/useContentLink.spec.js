import Vuex from 'vuex';
import { validateLinkObject } from 'kolibri.utils.validators';
import { PageNames } from '../../../src/constants';
import useContentLink from '../useContentLink';

const name = 'test';
const query = {
  keyword: 'word',
  prevName: 'notatest',
  prevParams: encodeURI(JSON.stringify({ id: 'id' })),
  prevQuery: encodeURI(JSON.stringify({ search: 'this' })),
};
const params = { lesson: 'that' };

const store = new Vuex.Store({
  state: {
    route: {
      name,
      params,
      query,
    },
  },
});

const { genContentLink } = useContentLink(store);

const topicLink = genContentLink(19, false);
const contentLink = genContentLink(88, true);

describe('genContentLink - generating for a topic (isLeaf != true)', () => {
  it('returns a valid link object', () => {
    expect(validateLinkObject(topicLink)).toBeTruthy();
  });

  it('returns an object with name pointing to PageName.TOPICS_TOPIC', () => {
    expect(topicLink.name).toEqual(PageNames.TOPICS_TOPIC);
  });

  it('returns a params object with the passed id', () => {
    expect(topicLink.params.id).toEqual(19);
  });
});

describe('genContentLink - generating for a topic (isLeaf == true)', () => {
  it('returns a valid link object', () => {
    expect(validateLinkObject(contentLink)).toBeTruthy();
  });

  it('returns an object with name pointing to PageName.TOPICS_CONTENT', () => {
    expect(contentLink.name).toEqual(PageNames.TOPICS_CONTENT);
  });

  it('returns a params object with the passed id', () => {
    expect(contentLink.params.id).toEqual(88);
  });
});
