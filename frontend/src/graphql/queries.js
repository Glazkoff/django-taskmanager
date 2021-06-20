import gql from "graphql-tag";

export const BOARDS_IN_TEAM = gql`
  query ($teamId: ID) {
    boardsInTeam(teamId: $teamId) {
      id
      name
      statusSet {
        id
        name
        taskSet {
          id
          body
        }
      }
    }
  }
`;

export const BOARD_BY_ID = gql`
  query ($boardId: ID) {
    board(boardId: $boardId) {
      id
      name
      statusSet {
        id
        name
      }
      taskSet {
        id
        storyPoints
        body
        status {
          id
          name
        }
      }
    }
  }
`;

export const BOARDS = gql`
  query {
    boards {
      id
      name
      statusSet {
        id
        name
        taskSet {
          id
          body
        }
      }
    }
  }
`;

export const TEAMS_LIST = gql`
  query {
    teams {
      id
      name
      boardSet {
        id
        name
      }
    }
  }
`;
