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
