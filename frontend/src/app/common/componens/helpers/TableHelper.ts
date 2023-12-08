export interface ITable {
    totalRecordsCount: number;
    currentPage: number;
    pageSize: number;
    predefinedRecordsCountPerPage: number[];
}

export interface ITableHelper {
    getSkipCount: () => number;
    getMaxResultCount: () => number;
    table: ITable;
}

export class TableHelper {

    table: ITable = {
        totalRecordsCount: 0,
        currentPage: 0,
        pageSize: 100,
        predefinedRecordsCountPerPage: [5, 10, 25, 50, 100, 250, 500],
    };

    getSkipCount(): number {
        if(!this.table.currentPage) {
            return 0;
        }
        return (this.table.currentPage - 1) * this.table.pageSize;
    }

    getMaxResultCount(): number {
        if(!this.table.currentPage) {
            return 0;
        }
        return (this.table.currentPage - 1) * this.table.pageSize;
    }
}
